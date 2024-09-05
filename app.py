import streamlit as st  # Streamlit library for creating the web application interface
import google.generativeai as genai  # Google Generative AI library to interact with the generative AI model
import os  # OS library for accessing environment variables like API keys
import PyPDF2 as pdf  # PyPDF2 library for handling and extracting text from PDF files
from dotenv import load_dotenv  # dotenv library for loading environment variables from a .env file
import json  # JSON library for formatting the output as a JSON string (if needed)

# Load environment variables from the .env file (e.g., API keys)
load_dotenv()

# Configure the Google Generative AI model with the API key from environment variables
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to send the resume and job description to the AI model and get a response
def get_gemini_repsonse(input):
    model = genai.GenerativeModel('gemini-pro')  # Load the AI model ('gemini-pro')
    response = model.generate_content(input)  # Generate content based on the provided input
    return response.text  # Return the text output from the AI model

# Function to extract text from an uploaded PDF resume
def input_pdf_text(uploaded_file):
    reader = pdf.PdfReader(uploaded_file)  # Initialize the PDF reader with the uploaded file
    text = ""  # Initialize an empty string to store the extracted text
    # Loop through each page in the PDF and extract the text
    for page in range(len(reader.pages)):
        page = reader.pages[page]
        text += str(page.extract_text())  # Extract and concatenate text from each page
    return text  # Return the full text extracted from the PDF

# Input prompt for the "Tell Me About the Resume" feature
input_prompt1 = """
You are an expert ATS (Applicant Tracking System) specializing in evaluating resumes for technical roles such as software engineering, data science, data analysis, and big data engineering. Your task is to analyze the provided resume against the given job description, focusing on accuracy and relevance to the role. The analysis should consider the competitive job market, providing clear and actionable feedback.

Please include the following in your response:

1. A percentage match indicating how well the resume aligns with the job description.
2. A list of missing keywords in resume that are there in the job description.
3. A concise profile summary that highlights the strengths and weaknesses of the resume.
4. Suggested skill improvements that the candidate can make to increase their chances of landing the job.

Use the following structured format for your response:

{{"JD Match": "%", \n
"Missing Keywords": [], \n
"Profile Summary": "", \n
"Skill Improvements": "[\\"Skill 1\\", \\"Skill 2\\", ...]" \n}}

The resume content is: {text}
The job description is: {jd}
"""


## Streamlit app interface setup
st.title("ATS Consultant")  # Title of the web app
st.text("AI ATS Consultant")  # Subtitle text

# Text area for users to paste the job description
jd = st.text_area("Job Description")

# File uploader for users to upload their PDF resume
uploaded_file = st.file_uploader("Please Upload Your Resume", type="pdf", help="Please upload a PDF")

# Submit button to trigger resume evaluation
submit = st.button("Submit")

# When the submit button is clicked
if submit:
    # Ensure a resume file has been uploaded
    if uploaded_file is not None:
        # Extract the text from the uploaded PDF resume
        text = input_pdf_text(uploaded_file)
        
        # Prepare the prompt for the AI model by filling in the resume text and job description
        input_prompt_filled = input_prompt1.format(text=text, jd=jd)
        
        # Get the AI-generated response for the resume and job description evaluation
        response = get_gemini_repsonse(input_prompt_filled)
        
        # Display the AI's evaluation on the Streamlit interface
        st.subheader(response)
