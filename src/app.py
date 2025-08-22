from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.modules.ocr import controller as ocr_controller

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(ocr_controller.router, prefix="/ocr")

@app.get("/")
def read_root():
    return {"status": "ok"}