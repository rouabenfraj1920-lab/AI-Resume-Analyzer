import streamlit as st
import hashlib
import os

from src.pdf_reader import extract_text_from_pdf
from src.rag.chunker import chunk_text
from src.rag.vector_store import (
    reset_collection,
    create_collection,
    add_chunks,
    search_chunks
)
from src.rag.query_expansion import expand_query
from src.llm.gemini_client import generate_response
from src.prompts.resume_prompt import build_resume_analysis_prompt
from src.llm.gemini_client import analyze_resume


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)

st.title("📄 AI Resume Analyzer")

st.sidebar.title("📄 AI Resume Analyzer")

st.sidebar.markdown("""
### About

This application analyzes resumes using:

- 📑 PDF Processing
- 🧠 RAG (Retrieval-Augmented Generation)
- 🔎 Semantic Search
- 🚀 Query Expansion
- 🎯 Cross-Encoder Reranking
- 🤖 Gemini LLM

Developed with Streamlit.
""")
st.sidebar.markdown("---")


# =========================================================
# SESSION STATE
# =========================================================

if "messages" not in st.session_state:
    st.session_state.messages = []

if "collection" not in st.session_state:
    st.session_state.collection = None

if "chunks" not in st.session_state:
    st.session_state.chunks = []

if "cv_id" not in st.session_state:
    st.session_state.cv_id = None

if "cv_name" not in st.session_state:
    st.session_state.cv_name = None
if "resume_analysis" not in st.session_state:
    st.session_state.resume_analysis = None
if "uploader_version" not in st.session_state:
    st.session_state.uploader_version = 0
# =========================================================
# CLEAR / NEW CV
# =========================================================

def clear_cv():
    st.session_state.messages = []
    st.session_state.collection = None
    st.session_state.chunks = []
    st.session_state.cv_id = None
    st.session_state.cv_name = None
    st.session_state.resume_analysis = None

    # Reset the uploader
    st.session_state.uploader_version += 1

    # Reset ChromaDB
    try:
        reset_collection()
    except Exception:
        pass

    # Delete temporary CV
    if os.path.exists("temp_cv.pdf"):
        try:
            os.remove("temp_cv.pdf")
        except Exception:
            pass

st.sidebar.button(
    "🗑️ Clear / New CV",
    on_click=clear_cv,
    use_container_width=True
)

# =========================================================
# UPLOAD CV
# =========================================================

st.write("Upload a CV and ask questions about the candidate.")

uploaded_file = st.file_uploader(
    "Upload your CV (PDF)",
    type=["pdf"],
    key=f"cv_uploader_{st.session_state.uploader_version}"
)


# =========================================================
# PROCESS CV ONLY IF IT IS NEW
# =========================================================

if uploaded_file is not None:

    # Read uploaded file
    file_bytes = uploaded_file.getvalue()

    # Create a unique ID for the uploaded CV
    cv_id = hashlib.md5(file_bytes).hexdigest()

    # Check if this is a new CV
    if st.session_state.cv_id != cv_id:

        st.session_state.cv_id = cv_id
        st.session_state.cv_name = uploaded_file.name

        # Clear previous conversation
        st.session_state.messages = []

        save_path = "temp_cv.pdf"

        with open(save_path, "wb") as f:
            f.write(file_bytes)

        # -----------------------------------------
        # PROCESSING
        # -----------------------------------------

        with st.spinner("⏳ Processing CV..."):

            cv_text = extract_text_from_pdf(save_path)

            print("\n===== EXTRACTED TEXT =====")
            print(cv_text[:2000])
            print("Text length:", len(cv_text))

            chunks = chunk_text(cv_text)

            print("\n===== CHUNKS COUNT =====")
            print("Number of chunks:", len(chunks))

            # Reset ChromaDB
            reset_collection()

            # Create new collection
            collection = create_collection()

            # Add chunks to vector database
            add_chunks(collection, chunks)
            with st.spinner("🤖 Analyzing resume..."):

                analysis_prompt = build_resume_analysis_prompt(cv_text)

                st.session_state.resume_analysis = analyze_resume(analysis_prompt)                          


            st.success("✅ Resume analyzed successfully!")

        # Save processed data in session state
        st.session_state.collection = collection
        st.session_state.chunks = chunks

        st.success(f"CV uploaded: {uploaded_file.name}")

    else:

        # CV already processed
        st.success(f"CV uploaded: {uploaded_file.name}")
# =========================================================
# DISPLAY RESUME ANALYSIS
# =========================================================

if st.session_state.resume_analysis is not None:

    resume_analysis = st.session_state.resume_analysis

    st.divider()
    st.subheader("📋 Resume Overview")

    # -----------------------------------------------------
    # PROFESSIONAL SUMMARY
    # -----------------------------------------------------

    st.markdown("### 👤 Professional Summary")

    summary = resume_analysis.professional_summary

    # Limit summary length for a cleaner interface
    if len(summary) > 350:
        summary = summary[:350].rsplit(" ", 1)[0] + "..."

    st.info(summary)

    # -----------------------------------------------------
    # QUICK STATISTICS
    # -----------------------------------------------------

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "🚀 Projects",
            len(resume_analysis.projects)
        )

    with col2:
        st.metric(
            "🛠 Skills",
            len(resume_analysis.skills)
        )

    with col3:
        st.metric(
            "🎓 Education",
            len(resume_analysis.education)
        )

    with col4:
        st.metric(
            "📜 Certifications",
            len(resume_analysis.certifications)
        )

    st.divider()

    # -----------------------------------------------------
    # PROJECTS
    # -----------------------------------------------------

    with st.expander(
        f"🚀 Projects ({len(resume_analysis.projects)})",
        expanded=True
    ):

        for project in resume_analysis.projects:

            st.markdown(f"#### {project.name}")

            st.write(project.description)

            if project.technologies:

                st.caption(
                    "🧰 " +
                    " • ".join(project.technologies)
                )

            st.divider()

    # -----------------------------------------------------
    # EDUCATION
    # -----------------------------------------------------

    with st.expander(
        f"🎓 Education ({len(resume_analysis.education)})"
    ):

        for education in resume_analysis.education:

            st.markdown(
                f"**{education.institution}**"
            )

            if education.field:
                st.write(
                    f"📚 {education.field}"
                )

            if education.period:
                st.caption(
                    f"📅 {education.period}"
                )

            st.divider()

    # -----------------------------------------------------
    # SKILLS
    # -----------------------------------------------------

    with st.expander(
        f"🛠 Skills ({len(resume_analysis.skills)})"
    ):

        # Display skills in columns
        skill_columns = st.columns(3)

        for i, skill in enumerate(resume_analysis.skills):

            with skill_columns[i % 3]:
                st.markdown(
                    f"• {skill}"
                )

    # -----------------------------------------------------
    # CERTIFICATIONS
    # -----------------------------------------------------

    with st.expander(
        f"📜 Certifications ({len(resume_analysis.certifications)})"
    ):

        for certification in resume_analysis.certifications:

            st.markdown(
                f"• {certification}"
            )


# =========================================================
# SIDEBAR CV INFORMATION
# =========================================================

if st.session_state.cv_name is not None:

    st.sidebar.success("✅ CV Loaded")

    st.sidebar.write(
        f"**File:** {st.session_state.cv_name}"
    )

    st.sidebar.write(
        f"**Chunks:** {len(st.session_state.chunks)}"
    )


# =========================================================
# DISPLAY CONVERSATION HISTORY
# =========================================================

for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.write(message["content"])


# =========================================================
# CHAT INPUT
# =========================================================

question = st.chat_input(
    "Ask a question about the CV"
)


# =========================================================
# PROCESS QUESTION
# =========================================================

if question:

    # Make sure a CV has been uploaded
    if st.session_state.collection is None:

        st.warning("Please upload a CV first.")

    else:

        # -----------------------------------------
        # USER MESSAGE
        # -----------------------------------------

        st.session_state.messages.append({
            "role": "user",
            "content": question
        })

        with st.chat_message("user"):
            st.write(question)


        # -----------------------------------------
        # QUERY EXPANSION
        # -----------------------------------------

        queries = expand_query(question)


        # -----------------------------------------
        # RETRIEVAL
        # -----------------------------------------

        context = search_chunks(
            st.session_state.collection,
            question,
            queries
        )


        # -----------------------------------------
        # PROMPT
        # -----------------------------------------

        prompt = f"""
You are an AI Resume Assistant.

Your task is to answer ONLY using the retrieved context.

Rules:
- Answer in English.
- Never invent information.
- Never guess dates or names.
- If the answer is incomplete, explicitly say it is incomplete.
- If the answer is not present in the context, reply:
"I don't have enough information."

Context:
{context}

Question:
{question}
"""


        # -----------------------------------------
        # GEMINI
        # -----------------------------------------

        with st.spinner("🤖 Generating answer..."):

            answer = generate_response(prompt)


        # -----------------------------------------
        # ASSISTANT MESSAGE
        # -----------------------------------------

        with st.chat_message("assistant"):
            st.write(answer)


        # Save assistant response
        st.session_state.messages.append({
            "role": "assistant",
            "content": answer
        })