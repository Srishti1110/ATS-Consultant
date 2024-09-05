# ATS Resume Expert: AI-Powered Resume Evaluation

## Overview

**ATS Resume Expert** is a web application designed to assist job seekers by analyzing their resumes in comparison to a job description. The app utilizes **Google's Gemini Pro Vision** generative AI model to provide comprehensive feedback and evaluate resume alignment with a given job description. The system can:

- Review a resume from a human resource perspective.
- Assess the percentage match of the resume with a job description.
- Highlight strengths, weaknesses, missing keywords, and other relevant insights for improvement.

### Key Features:
1. **AI-Powered Resume Review**: Uses the `gemini-pro-vision` model to analyze resumes and provide detailed feedback on how well a candidate's profile aligns with a specific job description.
2. **Applicant Tracking System (ATS) Evaluation**: The app evaluates how well the resume would pass through an ATS, providing a match percentage and listing missing keywords.
3. **PDF Resume Upload**: Allows users to upload their resume in PDF format, which is then converted to an image and processed by the AI model.
4. **Job Description Input**: Users can input a job description text that is used as the basis for evaluating the resume.
5. **Streamlit-Based UI**: A simple and user-friendly interface built using Streamlit.

## App Design

### 1. App Architecture
The application is divided into the following main components:

- **PDF Handling and Conversion**: Upload the resume (PDF), convert it into an image, and encode it in base64 format to pass to the AI model.
- **Generative AI Model Interaction**: Google’s Gemini AI model (`gemini-pro-vision`) is used to generate content and analyze the resume.
- **Streamlit User Interface**: Provides an easy-to-use interface for users to upload resumes, input job descriptions, and view AI-generated feedback.

### 2. App Flow
#### User Inputs:
- **Job Description**: Users enter a job description in a text area.
- **Resume Upload**: Users upload their resume in PDF format.

#### AI Processing:
- The uploaded PDF is converted into an image and sent to the Google Gemini AI model along with the job description and predefined prompts.
- The AI model processes the resume and returns a detailed response evaluating the candidate's fit for the job.

#### Outputs:
- **Human Resource Review**: Provides detailed feedback on the alignment between the resume and the job description.
- **ATS Evaluation**: Gives a percentage match of the resume based on ATS standards, including missing keywords and additional insights.

### 3. App Interface Design
The Streamlit app interface is minimalistic and user-friendly, containing:
- **Title and Header**: Sets the context for the application.
- **Text Area for Job Description**: Input box for users to paste the job description.
- **PDF Uploader**: A file uploader to accept PDF resumes.
- **Buttons for Different Actions**:
  - **"Tell Me About the Resume"**: For detailed feedback.
  - **"Percentage Match"**: To calculate the percentage match for ATS systems.
- **Results Section**: Displays the AI-generated feedback and evaluation.

## Technologies Used

- **Python**: Core language for building the backend and business logic.
- **Streamlit**: Provides a simple, interactive UI.
- **Google Generative AI**: For using the Gemini Pro Vision model to generate responses and evaluate resumes.
- **pdf2image**: Converts PDF resumes into images for AI processing.
- **Pillow (PIL)**: For handling images, particularly the first page of the PDF resume.
- **Base64**: Encoding images into base64 format for passing them to the AI model.
- **dotenv**: To manage API keys and other sensitive data securely.
