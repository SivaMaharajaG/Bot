# extract.py

import fitz  # PyMuPDF
import re

def extract_text_from_pdf(pdf_file):
    doc = fitz.open(stream=pdf_file.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def detect_qualification(text, qualifications):
    for q in qualifications:
        if re.search(rf"\b{re.escape(q)}\b", text, re.IGNORECASE):
            return q
    return None
