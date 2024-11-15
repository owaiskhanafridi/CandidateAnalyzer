import PyPDF2
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk

# Download necessary NLTK resources
nltk.download('stopwords')
nltk.download('punkt')

# Sample list of skills for demonstration (expand as needed)
SKILLS = [
    'Python', 'Data Analysis', 'Machine Learning', 'SQL', 'Java', 'Project Management', 
    'Communication', 'Time Management', 'Teamwork', 'JavaScript', 'C++', 'Leadership', 'NLP',
    'Deep Learning', 'Pandas', 'NumPy', 'Data Visualization', 'Power BI', 'Tableau', 'AWS', 'Azure'
]

def extract_text_from_pdf(pdf_path):
    """Extract text from a PDF file."""
    text = ""
    try:
        with open(pdf_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            for page in pdf_reader.pages:
                text += page.extract_text()
    except Exception as e:
        print("Error reading PDF file:", e)
    return text

def load_job_description(file_path):
    """Load job description text from a text file."""
    try:
        with open(file_path, 'r') as file:
            job_description = file.read()
        return job_description
    except Exception as e:
        print("Error reading job description file:", e)
        return ""

def clean_and_tokenize(text):
    """Clean and tokenize text, removing stopwords and special characters."""
    stop_words = set(stopwords.words("english"))
    words = word_tokenize(text)
    words = [word.lower() for word in words if word.isalnum() and word.lower() not in stop_words]
    return words

def extract_skills(text):
    """Identify skills in the given text based on the predefined SKILLS list."""
    words = set(clean_and_tokenize(text))
    found_skills = [skill for skill in SKILLS if skill.lower() in words]
    return found_skills

def calculate_skill_match(resume_skills, job_description_skills):
    """Calculate the percentage match based on common skills."""
    if not job_description_skills:
        return 0
    match_count = len(set(resume_skills) & set(job_description_skills))
    return (match_count / len(job_description_skills)) * 100

def main(pdf_path, job_description_path):
    # Extract text from the PDF resume
    resume_text = extract_text_from_pdf(pdf_path)

    # Load job description from text file
    job_description = load_job_description(job_description_path)

    # Extract skills from both resume and job description
    resume_skills = extract_skills(resume_text)
    job_description_skills = extract_skills(job_description)

    # Calculate the skill match percentage
    match_percentage = calculate_skill_match(resume_skills, job_description_skills)

    # Print results
    print("Resume Skills:", resume_skills)
    print("Job Description Skills:", job_description_skills)
    print(f"Skill Match: {match_percentage:.2f}%")

# Example usage:
pdf_path = 'Resume.pdf'  # Replace with the path to your PDF resume
job_description_path = 'job_description.txt'  # Replace with the path to your job description text file

main(pdf_path, job_description_path)
