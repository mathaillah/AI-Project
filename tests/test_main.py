from fastapi.testclient import TestClient
from src.app import app
import pytest
from unittest.mock import patch, MagicMock
import numpy as np

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

@patch('src.modules.ocr.service.preprocess_image')
@patch('src.modules.ocr.service.pytesseract.image_to_string')
def test_process_cv(mock_image_to_string, mock_preprocess_image):
    mock_preprocess_image.return_value = np.zeros((100, 100, 3), dtype=np.uint8)
    mock_image_to_string.return_value = "extracted text"

    with open("test.txt", "w") as f:
        f.write("test")

    with open("test.txt", "rb") as f:
        response = client.post("/ocr/process-cv", files={"file": ("test.txt", f, "text/plain")})

    assert response.status_code == 200
    assert response.json() == {"text": "extracted text"}

@patch('cv2.imread')
@patch('cv2.cvtColor')
@patch('cv2.split')
@patch('cv2.createCLAHE')
@patch('cv2.merge')
@patch('cv2.GaussianBlur')
@patch('cv2.threshold')
@patch('cv2.minAreaRect')
@patch('cv2.getRotationMatrix2D')
@patch('cv2.warpAffine')
def test_preprocess_image(mock_warpAffine, mock_getRotationMatrix2D, mock_minAreaRect, mock_threshold, mock_GaussianBlur, mock_merge, mock_createCLAHE, mock_split, mock_cvtColor, mock_imread):
    # Mock all the cv2 functions to avoid actual image processing
    mock_imread.return_value = np.zeros((100, 100, 3), dtype=np.uint8)
    mock_cvtColor.return_value = np.zeros((100, 100, 3), dtype=np.uint8)
    mock_split.return_value = [np.zeros((100, 100), dtype=np.uint8)] * 3
    mock_createCLAHE.return_value = MagicMock()
    mock_merge.return_value = np.zeros((100, 100, 3), dtype=np.uint8)
    mock_GaussianBlur.return_value = np.zeros((100, 100, 3), dtype=np.uint8)
    mock_threshold.return_value = (0, np.zeros((100, 100), dtype=np.uint8))
    mock_minAreaRect.return_value = ((0, 0), (0, 0), 0)
    mock_getRotationMatrix2D.return_value = np.zeros((2, 3), dtype=np.float32)
    mock_warpAffine.return_value = np.zeros((100, 100, 3), dtype=np.uint8)

    from src.modules.ocr.service import preprocess_image
    result = preprocess_image("dummy_path")
    assert result is not None

@patch('src.modules.ocr.service.preprocess_image')
@patch('src.modules.ocr.service.pytesseract.image_to_string')
def test_extract_text_from_image(mock_image_to_string, mock_preprocess_image):
    mock_preprocess_image.return_value = np.zeros((100, 100, 3), dtype=np.uint8)
    mock_image_to_string.return_value = "extracted text"

    from src.modules.ocr.service import extract_text_from_image
    result = extract_text_from_image("dummy_path")
    assert result == "extracted text"
