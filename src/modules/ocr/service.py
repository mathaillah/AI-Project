import pytesseract
from PIL import Image
import cv2
import numpy as np
import logging
import os

logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

def preprocess_image(image_path: str):
    """
    Performs pre-processing on an image file.
    """
    img = cv2.imread(image_path)
    if img is None:
        raise ValueError(f"Could not read image from path: {image_path}")

    # Image enhancement (contrast adjustment)
    lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
    l, a, b = cv2.split(lab)
    clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8, 8))
    cl = clahe.apply(l)
    limg = cv2.merge((cl, a, b))
    final = cv2.cvtColor(limg, cv2.COLOR_LAB2BGR)

    # Noise reduction (Gaussian blur)
    final = cv2.GaussianBlur(final, (5, 5), 0)

    # Deskewing
    gray = cv2.cvtColor(final, cv2.COLOR_BGR2GRAY)
    thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    coords = np.column_stack(np.where(thresh > 0))
    angle = cv2.minAreaRect(coords)[-1]
    if angle < -45:
        angle = -(90 + angle)
    else:
        angle = -angle
    (h, w) = img.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated = cv2.warpAffine(final, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)

    return rotated

def extract_text_from_image(image_path: str) -> str:
    """
    Extracts text from an image or PDF file using Tesseract OCR.
    """
    try:
        file_extension = os.path.splitext(image_path)[1].lower()

        if file_extension == '.pdf':
            text = pytesseract.image_to_string(image_path, lang='eng+ind')
        else:
            preprocessed_image = preprocess_image(image_path)
            pil_image = Image.fromarray(cv2.cvtColor(preprocessed_image, cv2.COLOR_BGR2RGB))
            text = pytesseract.image_to_string(pil_image, lang='eng+ind')
        return text
    except Exception as e:
        logging.error(f"Error extracting text from {image_path}: {e}", exc_info=True)