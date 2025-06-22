# chatbot.py

import streamlit as st
from datetime import datetime
from extract import extract_text_from_pdf, detect_qualification
from websearch import search_web
from database import save_chat
from export import export_chat_as_pdf

# Static company mapping
placement_data = {
    "B.E": ["TCS", "Infosys", "Wipro", "Zoho"],
    "B.Tech": ["TCS", "Cognizant", "Zoho"],
    "MCA": ["Infosys", "TCS", "HCL"],
    "B.Sc": ["HCL", "Wipro"],
    "BCA": ["HCL", "TCS"],
    "M.E": ["Zoho", "TCS", "Infosys"]
}

def chat_interface():
    st.title("🤖 IT Placement Chatbot")

    # Upload Resume
    resume = st.file_uploader("📥 Upload Resume (PDF)", type=["pdf"])
    if resume:
        text = extract_text_from_pdf(resume)
        qualification = detect_qualification(text, list(placement_data.keys()))
        if qualification:
            st.session_state.last_qualification = qualification
            st.success(f"Detected Qualification: {qualification}")
        else:
            st.warning("Could not detect qualification.")

    # Initialize chat history
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    # User query
    query = st.text_input("You:")
    if query:
        st.session_state.chat_history.append(("You", query))

        # Detect qualification
        qualification = None
        for q in placement_data:
            if q.lower() in query.lower():
                qualification = q
                break
        if not qualification:
            qualification = st.session_state.get("last_qualification", None)

        # Generate response
        if qualification:
            companies = placement_data.get(qualification, [])
            response = f"Based on your qualification ({qualification}), companies hiring:\n"
            response += "\n".join(f"- {c}" for c in companies)
        else:
            response = "Sorry, I couldn’t find your qualification. Please upload your resume."

        # Add web search
        web_info = search_web(f"{qualification} IT placement companies Tamil Nadu") if qualification else []
        if web_info:
            response += "\n\n📡 Latest Info from Web:\n"
            for line in web_info:
                response += f"- {line}\n"

        # Save & display
        st.session_state.chat_history.append(("Bot", response))
        save_chat(st.session_state.user_id, query, response, datetime.now().isoformat())

    # Show chat
    st.markdown("### 🗨️ Chat History")
    for speaker, msg in st.session_state.chat_history:
        st.markdown(f"**{speaker}:** {msg}")

    # Export PDF
    if st.button("📤 Export Chat to PDF"):
        export_chat_as_pdf(st.session_state.chat_history, st.session_state.username)
