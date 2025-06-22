# export.py

from fpdf import FPDF
import os
from datetime import datetime

def export_chat_as_pdf(chat_history, username):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, txt=f"Chat History for {username}", ln=True, align='C')
    pdf.ln(10)

    for speaker, message in chat_history:
        label = f"{speaker}:"
        pdf.multi_cell(0, 10, f"{label} {message}")
        pdf.ln(1)

    filename = f"{username}_chat_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
    filepath = os.path.join(".", filename)
    pdf.output(filepath)

    with open(filepath, "rb") as file:
        return file.read(), filename
