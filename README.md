# ATS Consultant: AI-Powered Resume Evaluation

## Overview

**ATS Consultant** is a web-based tool designed to evaluate resumes against specific job descriptions using AI. This app simulates the role of an Applicant Tracking System (ATS), helping job seekers assess how well their resumes align with job postings in the tech field. The system analyzes key elements such as keyword matching, profile summary, and skill improvements, providing comprehensive and actionable feedback to enhance the resume.

The application uses Google's **Generative AI (gemini-pro)** to perform in-depth analysis of resumes in PDF format and compare them against job descriptions provided by users. The app focuses on technical roles such as **software engineering**, **data science**, **data analysis**, and **big data engineering**.

## Features

- **AI-Powered Resume Review**: Utilizes Google's gemini-pro model to generate detailed feedback on how well a candidate's resume matches a job description.
- **ATS Simulation**: Provides a percentage match based on keyword alignment and evaluates the profile's strengths and weaknesses.
- **PDF Upload**: Allows users to upload their resumes in PDF format, which is then processed by the AI for analysis.
- **Skill Suggestions**: Highlights areas of improvement, offering suggested skills that candidates can add to strengthen their profiles.
- **Streamlit-Based Interface**: A simple and user-friendly UI for job seekers to upload resumes and receive instant feedback.

## App Architecture

The application is divided into three main components:

1. **PDF Handling**: Users upload their resume as a PDF. The application extracts text from the file using PyPDF2.
2. **Generative AI Integration**: The extracted resume text and job description are passed to Google's gemini-pro model for evaluation.
3. **Streamlit User Interface**: A lightweight and interactive web interface is provided for easy interaction and result display.

## App Flow

1. **User Inputs**:
    - **Job Description**: Users input the job description in a text area.
    - **Resume Upload**: Users upload their resume in PDF format.
    
2. **AI Processing**:
    - The uploaded PDF is converted to text, and both the resume text and job description are passed to the AI model.
    - The AI analyzes the resume and returns feedback in a structured format.
    
3. **Outputs**:
    - **JD Match Percentage**: Shows how closely the resume matches the job description.
    - **Missing Keywords**: Lists any keywords present in the job description but missing from the resume.
    - **Profile Summary**: Provides a brief analysis of the resume’s strengths and weaknesses.
    - **Skill Improvements**: Offers suggestions on which skills the candidate can improve or add.

## Technologies Used

- **Python**: Core programming language for the backend.
- **Streamlit**: Provides a simple and interactive web interface.
- **Google Generative AI**: Utilized for the `gemini-pro` model to generate feedback and analysis.
- **PyPDF2**: Extracts text from PDF resumes for processing.
- **dotenv**: Manages environment variables like API keys securely.
- **Pillow (PIL)**: Handles image processing if required (optional).

## Installation and Setup

To set up and run this application locally, follow these steps:

### Prerequisites

- Python 3.x
- Google Cloud API Key for Generative AI
- streamlit
- google-generativeai
- PyPDF2

### Steps
1. **Clone the Repository:** 

  - git clone https://github.com/yourusername/ats-consultant.git

2. **Navigate to the Project Directory:**

 -  cd ats-consultant

3. **Install the Required Dependencies:**

  - pip install -r requirements.txt

4. **Set up Environment Variables:**

 -  Create a .env file in the root directory and add your Google API key:
  - GOOGLE_API_KEY=your-google-api-key

5. **Run the Application:**

 -  streamlit run app.py

## Usage
- Upload Resume: Upload your resume as a PDF.
- Enter Job Description: Paste the relevant job description into the text area.
- Submit: Click the "Submit" button to see the evaluation results.

### Example Output
The output is provided in a structured JSON format with key insights such as:

{
  "JD Match": "85%",
  "Missing Keywords": ["Python", "Machine Learning"],
  "Profile Summary": "The resume has a strong background in data science...",
  "Skill Improvements": ["Python", "Big Data"]
}








