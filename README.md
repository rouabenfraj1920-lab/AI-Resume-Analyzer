# 📄 AI Resume Analyzer

An **AI-powered Resume Analyzer** that combines **Large Language Models (LLMs)** and **Retrieval-Augmented Generation (RAG)** to analyze resumes and answer questions based on their content.

The application allows users to upload a CV in PDF format, automatically extract and structure its information, and interact with it through a conversational interface.

---

## ✨ Features

- 📑 PDF resume processing
- 🤖 AI-powered resume analysis
- 🧠 Retrieval-Augmented Generation (RAG)
- 🔎 Semantic search
- 🚀 Query expansion
- 🎯 Cross-encoder reranking
- 🗂️ Vector storage with ChromaDB
- 💬 Conversational CV question answering
- 📊 Structured resume analysis

The resume analysis includes:

- 👤 Professional Summary
- 🛠️ Skills
- 🚀 Projects
- 🎓 Education
- 📜 Certifications

---

## 🧠 How It Works

The application follows an end-to-end RAG pipeline:

```text
PDF Resume
     │
     ▼
Text Extraction
     │
     ▼
Text Chunking
     │
     ▼
Vector Embeddings
     │
     ▼
ChromaDB
     │
     │
User Question
     │
     ▼
Query Expansion
     │
     ▼
Semantic Retrieval
     │
     ▼
Cross-Encoder Reranking
     │
     ▼
Relevant Context
     │
     ▼
Gemini LLM
     │
     ▼
Grounded Answer
```

For structured resume analysis, the extracted CV content is also processed by Gemini using a **Pydantic response schema** to produce consistent structured information.

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core development |
| Streamlit | Web interface |
| Google Gemini | LLM and AI generation |
| Hugging Face Transformers | NLP and model integration |
| Sentence Transformers | Vector embeddings |
| ChromaDB | Vector database |
| Cross-Encoder | Result reranking |
| PyMuPDF | PDF text extraction |
| Pydantic | Structured output validation |
| python-dotenv | Environment variable management |

---

## 📂 Project Structure

```text
AI-Resume-Analyzer/
│
├── app.py
│
├── src/
│   ├── pdf_reader.py
│   │
│   ├── llm/
│   │   └── gemini_client.py
│   │
│   ├── models/
│   │   └── resume_models.py
│   │
│   ├── prompts/
│   │   └── resume_prompt.py
│   │
│   └── rag/
│       ├── chunker.py
│       ├── vector_store.py
│       ├── query_expansion.py
│       └── reranker.py
│
├── requirements.txt
├── .gitignore
└── README.md
```

---



## 💬 Example Questions

After uploading a resume, you can ask questions such as:

- What projects has the candidate worked on?
- What are the candidate's main technical skills?
- What is the candidate's educational background?
- What certifications does the candidate have?
- What technologies were used in the projects?
- What is the candidate's professional profile?

---

## 🎯 Key Learning Outcomes

This project was a valuable hands-on experience in building an **end-to-end RAG application**, from document processing and embeddings to retrieval and LLM generation.

It helped me understand how different components work together in a practical AI system:

- 🔎 Expand user queries to improve retrieval
- 🧠 Retrieve relevant information using semantic search
- 🎯 Rerank retrieved results for better relevance
- 🤖 Provide grounded context to an LLM
- 📊 Generate structured outputs using Pydantic
- 🤗 Integrate Hugging Face models into an AI pipeline
- 💻 Build an interactive AI application with Streamlit

---

## 🔮 Future Improvements

- 🌐 Deploy the application online
- 📊 Add resume scoring
- 🎯 Add Job Description matching
- 📈 Add skill-gap analysis
- 📁 Support multiple resumes
- 👥 Add recruiter-oriented candidate comparison

---

## 👩‍💻 Author

**Roua Ben Fraj**

Computer Science Engineering Student | AI & Tech Enthusiast | IEEE CS Chair

📍 Tunis, Tunisia

🔗 [GitHub](https://github.com/rouabenfraj1920-lab)

---

⭐ If you find this project interesting, feel free to explore the repository!
