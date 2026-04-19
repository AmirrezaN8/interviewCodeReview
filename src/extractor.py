import fitz
import docx
import os
import re
import json

#text from pdf extractor function
def extract_text_from_pdf(file_path):
    text = ""
    try:
        with fitz.open(file_path) as pdf_document:
            for page in pdf_document:
                text += page.get_text("text")+ "\n"

    except Exception as e:
        print(f"Error reading pdf from {file_path}: {e}")
    return text


#text from docx extractor function
def extract_text_from_docx(file_path):
    text = ""
    try:
        doc = docx.Document(file_path)
        for para in doc.paragraphs:
            text += para.text + "\n"
    except Exception as e:
        print(f"Error reading docx from {file_path}: {e}")
    return text

#github link extractor function from text
def find_github_links(text):
    github_links = r"github\.com/[A-Za-z0-9_.-]+"
    match = re.search(github_links,text, re.IGNORECASE)

    if match:
        return match.group(0).rstrip("/")
    return None

#extracting github username from the files in the given directory and returning the results in json format
def process_resumes(directory_path):
    results = []

    for filename in os.listdir(directory_path):
        file_path = os.path.join(directory_path, filename)

        if os.path.isdir(file_path):
            continue

        rawtxt = ""

        if filename.lower().endswith('.pdf'):
            rawtxt = extract_text_from_pdf(file_path)
        elif filename.lower().endswith('.docx'):
            rawtxt = extract_text_from_docx(file_path)
        else:
            continue

        username = find_github_links(rawtxt)

        if username:
            results.append({
                "candidate_filename": filename,
                "github_url": f"https://github.com/{username}",
                "github_username": username,
                "STATUS": "success"
            })
        else:
            results.append({
                "candidate_filename": filename,
                "github_url": None,
                "github_username": None,
                "STATUS": "failure"
            })

    return json.dumps(results, indent=2)
