from fastapi import APIRouter, UploadFile, File
from .service import extract_text_from_image
import shutil
import tempfile
import os
import uuid
from datetime import datetime

router = APIRouter()

@router.post("/process-cv")
async def process_cv(file: UploadFile = File(...)):
    """
    Processes a single CV file and returns the extracted text.
    """
    temp_file_path = ""
    try:
        # Create a temporary file to store the uploaded file
        with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(file.filename)[1]) as temp_file:
            shutil.copyfileobj(file.file, temp_file)
            temp_file_path = temp_file.name

        extracted_text = extract_text_from_image(temp_file_path)
    finally:
        # Clean up the temporary file
        if temp_file_path and os.path.exists(temp_file_path):
            os.unlink(temp_file_path)

    # Save the extracted text to a file in ocr_results folder
    results_dir = "ocr_results"
    os.makedirs(results_dir, exist_ok=True)

    # Generate a unique filename
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    unique_id = str(uuid.uuid4())[:8]
    output_filename = f"ocr_result_{timestamp}_{unique_id}.txt"
    output_filepath = os.path.join(results_dir, output_filename)

    with open(output_filepath, "w", encoding="utf-8") as f:
        f.write(extracted_text)

    return {"text": extracted_text, "saved_to": output_filepath}
