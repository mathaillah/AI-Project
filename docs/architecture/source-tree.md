## Project Structure (Actual)

```text
project-root/
├── src/
│   ├── main.py                 # Main application entry point
│   ├── app.py                  # FastAPI application instance
│   ├── modules/                # Feature modules (e.g., ocr, cv_processing)
│   │   ├── ocr/
│   │   │   ├── __init__.py
│   │   │   ├── controller.py   # API endpoints for OCR
│   │   │   ├── service.py      # Business logic for OCR
│   │   │   └── models.py       # Data models for OCR
│   │   └── cv_processing/
│   │       ├── __init__.py
│   │       ├── controller.py
│   │       ├── service.py
│   │       └── models.py
│   ├── shared/                 # Shared utilities, DTOs, interfaces
│   │   ├── __init__.py
│   │   ├── dtos.py
│   │   ├── interfaces.py
│   │   └── utils.py
│   ├── config/                 # Application configuration
│   │   └── __init__.py
│   │   └── settings.py
│   └── database/               # Database connection and migrations
│       ├── __init__.py
│       └── connection.py
├── tests/                      # Unit and integration tests
├── .env.example                # Environment variables example
├── requirements.txt            # Project dependencies
├── Dockerfile                  # Docker configuration
├── README.md                   # Project README
```
