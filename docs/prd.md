# My OCR App Product Requirements Document (PRD)

### Goals and Background Context

#### Goals

*   To develop an OCR-based CV processing application capable of extracting information from various general CV templates.
*   To convert extracted CV data into a specific, standardized template.
*   To support both single and bulk CV processing.
*   To achieve high accuracy in OCR and data extraction, adapting to diverse CV layouts and formats.
*   To support text recognition in both English and Bahasa Indonesia, including mixed-language documents.

#### Background Context

The primary challenge this project addresses is the significant difficulty in extracting structured information from the wide variety of CV templates currently in use, as there is no universal standard. This necessitates a solution capable of intelligently adapting to diverse layouts and formats. The proposed application aims to solve this by leveraging a learning-based system (AI/ML) that can understand and extract relevant data from unstructured or semi-structured CVs. A key focus will be on ensuring paramount accuracy in both the OCR process and subsequent data extraction. Furthermore, the system is designed to be user-friendly, providing intuitive interfaces for CV and template input, and clear presentation of processed outputs.

#### Change Log

| Date       | Version | Description          | Author |
| :--------- | :------ | :------------------- | :----- |
| 2025-08-22 | 1.0     | Initial Draft of PRD | John   |

---

### Requirements

#### Functional

The system **shall** be able to:

*   **FR1: CV Input:**
    *   FR1.1: Allow users to upload single CV files.
    *   FR1.2: Allow users to upload multiple CV files for bulk processing.
    *   FR1.3: Accept various CV file formats (e.g., PDF, DOCX, common image formats).
*   **FR2: Template Definition:**
    *   FR2.1: Allow users to upload a target template file (e.g., DOCX, PDF) to define the desired output structure.
    *   FR2.2: Provide a visual template builder for users to define their target template fields.
    *   FR2.3: Allow users to define target template fields by simply listing them (e.g., in a text box).
*   **FR3: OCR Processing:**
    *   FR3.1: Perform Optical Character Recognition (OCR) on uploaded CVs.
    *   FR3.2: Handle scanned documents through pre-processing steps (image enhancement, noise reduction, deskewing).
    *   FR3.3: Support text recognition for both English and Bahasa Indonesia, including documents with mixed languages.
*   **FR4: Data Extraction (Learning Model):**
    *   FR4.1: Utilize Named Entity Recognition (NER) to identify and extract specific entities from the CV text.
    *   FR4.2: Extract the following confirmed entities:
        *   Personal Information (Full Name, Email, Phone, LinkedIn, Location)
        *   Summary/Objective
        *   Work Experience (Job Title, Company Name, Location, Start Date, End Date, Job Description)
        *   Education (Degree/Qualification, Major/Field of Study, University/Institution Name, Location, Graduation Date)
        *   Skills (Technical Skills, Soft Skills, Languages)
        *   Projects (Project Title, Project Description, Role in Project, Technologies Used)
        *   Awards/Certifications (Award/Certification Name, Issuing Organization, Date Issued)
    *   FR4.3: Adapt to and learn from various CV layouts and formats to improve extraction accuracy over time.
*   **FR5: Output Generation:**
    *   FR5.1: Generate new CVs formatted according to the user-defined target template.
    *   FR5.2: Provide a preview of the extracted data mapped to the new template before final download.
    *   FR5.3: Allow users to download the converted CVs in specified formats (e.g., DOCX, PDF, CSV).
*   **FR6: User Feedback & Management:**
    *   FR6.1: Display a dashboard for bulk processing, showing the status of each CV (e.g., "Processing", "Success", "Failed").

#### Non Functional

The system **shall** be:

*   **NFR1: Accuracy:**
    *   NFR1.1: Achieve the highest possible accuracy in OCR text recognition.
    *   NFR1.2: Achieve high accuracy in extracting specified entities from diverse CV layouts.
*   **NFR2: Technology Stack:**
    *   NFR2.1: Be built using Python and FastAPI.
    *   NFR2.2: Primarily utilize open-source technologies (e.g., Tesseract, NLTK, Sastrawi).
*   **NFR3: Performance:**
    *   NFR3.1: Process single CVs efficiently, providing quick results.
    *   NFR3.2: Process bulk CVs in a timely manner, with clear progress indication.
*   **NFR4: Scalability:**
    *   NFR4.1: Be designed to handle increasing volumes of CV uploads and processing requests.
*   **NFR5: Maintainability:**
    *   NFR5.1: Allow for easy updates and retraining of the Learning Model as new CV templates or data patterns emerge.
    *   NFR5.2: Allow for dynamic changes to the target template by the user.
*   **NFR6: Usability:**
    *   NFR6.1: Provide an intuitive and user-friendly interface for all functionalities.
*   **NFR7: Security:**
    *   NFR7.1: Handle sensitive personal data within CVs securely (though specific security measures were not detailed, this is an inherent NFR for such an application).

---

### User Interface Design Goals

#### Overall UX Vision

The application aims to provide an intuitive, efficient, and highly user-friendly experience for processing Curriculum Vitae documents. The design will prioritize clarity, ease of use, and a streamlined workflow, ensuring that users can quickly and accurately convert diverse CV formats into their standardized templates.

#### Key Interaction Paradigms

The primary interaction paradigms will focus on direct manipulation and clear feedback. Users will engage with the system through straightforward actions such as file uploads, drag-and-drop functionalities (for the template builder), and immediate visual feedback on processing status and extracted data. The interface will guide users through each step of the CV conversion process.

#### Core Screens and Views

Based on the functional requirements, the most critical screens and views include:

*   **CV Upload Screen:** For both single and bulk CV submissions.
*   **Template Definition Screen:** Offering options for template file upload, a visual template builder, and direct text input for field definitions.
*   **Processed CV Preview Screen:** To allow users to review extracted data mapped to the new template before finalization.
*   **Download Results Screen:** For accessing converted CVs in various formats.
*   **Bulk Processing Dashboard:** To monitor the status and progress of multiple CV conversions.

#### Accessibility: None

*(Assumption: No specific accessibility requirements were discussed. Basic web accessibility best practices will be followed by default.)*

#### Branding

*(Assumption: No specific branding elements or style guides were provided. A clean, modern, and professional aesthetic will be adopted.)*

#### Target Device and Platforms: Web Responsive

*(Assumption: The application will be primarily web-based and designed to be responsive across various devices, ensuring usability on desktops, tablets, and mobile browsers.)*

---

### Technical Assumptions

#### Repository Structure: Polyrepo

*(Assumption: For an initial single application, a Polyrepo structure (a single repository for this application) is assumed for simplicity. A Monorepo could be considered for future expansion if multiple related services are planned.)*

#### Service Architecture: Monolith

*(Assumption: Given the scope of a single OCR application, a monolithic service architecture is assumed for the initial MVP to simplify development and deployment. This can be refactored into microservices or serverless functions in the future if scalability or independent deployment needs arise.)*

#### Testing Requirements: Unit + Integration

*(Assumption: To ensure high accuracy and reliability, comprehensive testing including both unit tests (for individual components) and integration tests (for interactions between components) will be required. Full end-to-end testing will be considered as the project matures.)*

#### Additional Technical Assumptions and Requests

*   **Programming Language:** Python will be the primary programming language for the backend.
*   **Web Framework:** FastAPI will be used for building the web services and APIs.
*   **OCR Engine:** Tesseract will be utilized for Optical Character Recognition.
*   **Natural Language Processing (NLP) Libraries:** NLTK will be used for Named Entity Recognition (NER), and Sastrawi will be used specifically for Indonesian language processing.
*   **Open-Source Preference:** All core technologies and libraries should primarily be open-source where feasible.
*   **Deployment Target:** The specific deployment environment (e.g., cloud provider, on-premise) is yet to be determined and will be a key decision for the Architect.

---

### Epic List

Here is a proposed list of Epics for the project, each with a brief goal statement:

*   **Epic 1: Foundation & Core OCR**
    *   *Goal:* To establish the basic application structure, set up the OCR engine with pre-processing, and implement the core text recognition for single CVs.
*   **Epic 2: Data Extraction & Learning Model V1**
    *   *Goal:* To implement the initial Learning Model to extract confirmed entities from the OCR text, focusing on a basic set of entities.
*   **Epic 3: Template Mapping & Output Generation**
    *   *Goal:* To develop the functionality to map extracted data to a user-defined template and generate the final output in various formats.
*   **Epic 4: Bulk Processing & UI Enhancements**
    *   *Goal:* To implement bulk CV upload and processing capabilities, along with the dashboard and advanced UI features.
*   **Epic 5: Model Refinement & Multi-Language Optimization**
    *   *Goal:* To continuously enhance the intelligence and reliability of the data extraction process through training data and optimizing multi-language support.

---

### Checklist Results Report

This section incorporates the findings from the Product Owner (PO) Master Validation Checklist that was run earlier. This report provides a comprehensive assessment of the project's readiness for development.

*(This section will reference the `po_checklist_report.md` file generated previously.)*

---

### Next Steps

#### UX Expert Prompt

@ux-expert: Please review this Product Requirements Document (PRD) to understand the user interface design goals and functional requirements. Your task is to elaborate on the UI/UX vision, create detailed wireframes, prototypes, and front-end specifications based on the requirements outlined in this PRD.

#### Architect Prompt

@architect: Please review this Product Requirements Document (PRD) to understand the functional, non-functional, and technical assumptions. Your task is to design the system architecture, including backend, database, API, and deployment considerations, ensuring alignment with the requirements and technical assumptions outlined in this PRD.
