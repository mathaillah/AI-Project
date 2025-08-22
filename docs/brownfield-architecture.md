# My OCR App Brownfield Architecture Document

## Introduction

This document captures the CURRENT STATE of the My OCR App codebase, including technical debt, workarounds, and real-world patterns. It serves as a reference for AI agents working on enhancements.

### Document Scope

Focused on areas relevant to the "My OCR App" project as described in `prd.md`.

### Change Log

| Date       | Version | Description                 | Author    |
| ---------- | ------- | --------------------------- | --------- |
| 2025-08-22 | 1.0     | Initial brownfield analysis | Architect |

## Quick Reference - Key Files and Entry Points

### Critical Files for Understanding the System

- **Main Entry**: `src/main.py` (or equivalent for FastAPI)
- **Configuration**: `src/config/` (assumed location for configuration files)
- **Core Business Logic**: `src/modules/` (assumed location for feature modules)
- **API Definitions**: `src/modules/*/controller.py` (assumed location for API endpoints)
- **Database Models**: `src/modules/*/entity.py` (assumed location for database entities/models)
- **Key Algorithms**: `src/ocr/` (assumed location for OCR related logic)

### If PRD Provided - Enhancement Impact Areas

(No specific enhancement PRD was provided, so this section is not applicable.)

## High Level Architecture

### Technical Summary

This system's overall architecture style is a modular backend service, initially monolithic, designed to evolve. It leverages Python with FastAPI for the backend, integrating Tesseract for OCR and NLTK/Sastrawi for NLP. The system aims for high accuracy in CV data extraction and conversion to standardized templates, supporting both English and Bahasa Indonesia.

### Actual Tech Stack (from package.json/requirements.txt)

| Category  | Technology | Version | Notes                                      |
| --------- | ---------- | ------- | ------------------------------------------ |
| Language  | Python     | 3.x     | Primary development language               |
| Framework | FastAPI    | 0.x     | Web services and APIs                      |
| OCR Engine| Tesseract  | 5.x     | Optical Character Recognition              |
| NLP       | NLTK       | 3.x     | Named Entity Recognition                   |
| NLP       | Sastrawi   | 1.x     | Indonesian language processing             |
| Database  | PostgreSQL | 15.x    | Relational Database (as per architecture.md)|
| ORM       | TypeORM    | 0.3.x   | Object-Relational Mapper (as per architecture.md)|

### Repository Structure Reality Check

- Type: Polyrepo
- Package Manager: pip (assumed)
- Notable: A single repository for this application, as per PRD assumption for simplicity.

## Source Tree and Module Organization

### Project Structure (Actual)

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

### Key Modules and Their Purpose

- **OCR Module (`src/modules/ocr/`)**: Handles the core OCR processing, including Tesseract integration and pre-processing steps.
- **CV Processing Module (`src/modules/cv_processing/`)**: Manages the overall CV processing workflow, including data extraction and output generation.
- **Shared Module (`src/shared/`)**: Contains common utilities, data transfer objects (DTOs), and interfaces used across different modules.
- **Config Module (`src/config/`)**: Manages application settings and environment-specific configurations.
- **Database Module (`src/database/`)**: Handles database connections, migrations, and ORM setup.

## Data Models and APIs

### Data Models

- **GenericDataModel**: See `architecture.md#data-models` for a conceptual model. Specific data models for CV entities (e.g., PersonalInfo, WorkExperience) will be defined within their respective modules (e.g., `src/modules/cv_processing/models.py`).

### API Specifications

- **REST API Spec**: See `architecture.md#rest-api-spec` for the OpenAPI 3.0 specification. Specific endpoints will be defined within the `controller.py` files of each module.

## Technical Debt and Known Issues

(Based on assumptions, as no actual code analysis was performed)

### Critical Technical Debt

1.  **OCR Pre-processing Optimization**: Initial pre-processing might be basic and require optimization for diverse CV layouts.
2.  **Learning Model Integration**: The initial data extraction model might be tightly coupled and require refactoring for better modularity and retraining capabilities.

### Workarounds and Gotchas

-   **Tesseract Installation**: Tesseract requires external installation and configuration, which can be a setup hurdle.
-   **Language Support**: Ensuring consistent and accurate multi-language (English and Bahasa Indonesia) OCR and NLP might require fine-tuning.

## Integration Points and External Dependencies

### External Services

| Service    | Purpose                               | Integration Type | Key Files/Libraries                               |
| ---------- | ------------------------------------- | ---------------- | ------------------------------------------------- |
| Tesseract  | Optical Character Recognition         | Library/CLI      | Python `pytesseract` library, Tesseract executable |
| NLTK       | Named Entity Recognition              | Library          | Python `nltk` library                             |
| Sastrawi   | Indonesian Language Processing        | Library          | Python `Sastrawi` library                         |
| PostgreSQL | Database (as per architecture.md)     | ORM/Driver       | `sqlalchemy`, `psycopg2` (assumed)                |

### Internal Integration Points

-   **Frontend Communication**: REST API on port 3000 (as per `architecture.md`), expects specific headers.
-   **Database Interaction**: Handled via ORM (TypeORM in `architecture.md`, but `sqlalchemy` is common for Python) within service layers.

## Development and Deployment

### Local Development Setup

1.  **Clone Repository**: `git clone <repository-url>`
2.  **Install Dependencies**: `pip install -r requirements.txt`
3.  **Install Tesseract**: Follow Tesseract installation guide for your OS.
4.  **Run Application**: `uvicorn main:app --reload` (assuming `main.py` and `app` instance)
5.  **Environment Variables**: Set up `.env` file based on `.env.example`.

### Build and Deployment Process

-   **Build Command**: `docker build -t my-ocr-app .` (assuming Docker for containerization)
-   **Deployment**: Blue/Green Deployment via GitHub Actions (as per `architecture.md`).
-   **Environments**: Dev, Staging, Prod.

## Testing Reality

### Current Test Coverage

-   Unit Tests: Expected to be high (as per `architecture.md` goal of >80%)
-   Integration Tests: Expected to be significant (as per `architecture.md`)
-   E2E Tests: None (initially, as per `architecture.md`)

### Running Tests

```bash
pytest           # Runs unit and integration tests (assumed pytest framework)
```

## If Enhancement PRD Provided - Impact Analysis

(No specific enhancement PRD was provided, so this section is not applicable.)

## Appendix - Useful Commands and Scripts

### Frequently Used Commands

```bash
# Local Development
uvicorn main:app --reload

# Dependency Management
pip install -r requirements.txt
pip freeze > requirements.txt

# Testing
pytest

# Docker
docker build -t my-ocr-app .
docker run -p 8000:8000 my-ocr-app
```

### Debugging and Troubleshooting

-   **Logs**: Application logs will be output to console or configured logging system.
-   **Debug Mode**: FastAPI debug mode can be enabled via environment variables.
-   **Common Issues**: Refer to Tesseract documentation for OCR-specific issues.
