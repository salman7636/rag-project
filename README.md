# 🤖 RAG Document AI

An AI-powered document question-answering system that allows users to upload PDF documents and interact with them using natural language.

The application uses **Retrieval-Augmented Generation (RAG)** to retrieve relevant information from uploaded documents and generate accurate, context-aware answers using **Google Gemini**.

---

## 🚀 Features

- 📄 Upload one or multiple PDF documents
- 🔍 Extract text from PDF files
- ✂️ Split documents into smaller text chunks
- 🧠 Generate semantic embeddings
- 🗃️ Store embeddings using FAISS
- 🔎 Retrieve relevant document chunks
- 🤖 Generate answers using Google Gemini
- 💬 Chat with uploaded documents
- 📝 Generate document summaries
- 📚 Display relevant sources and page numbers
- 🌐 Streamlit-based web interface
- 🔐 API keys stored securely using environment variables / Streamlit Secrets

---

## 🏗️ Architecture

The application follows this pipeline:

```text
                  ┌──────────────────┐
                  │   PDF Document   │
                  └────────┬─────────┘
                           │
                           ▼
                  ┌──────────────────┐
                  │  Text Extraction │
                  │   PyPDFLoader    │
                  └────────┬─────────┘
                           │
                           ▼
                  ┌──────────────────┐
                  │   Text Chunking  │
                  │ Recursive Splitter│
                  └────────┬─────────┘
                           │
                           ▼
                  ┌──────────────────┐
                  │    Embeddings    │
                  │ Hugging Face     │
                  └────────┬─────────┘
                           │
                           ▼
                  ┌──────────────────┐
                  │   FAISS Vector   │
                  │      Store       │
                  └────────┬─────────┘
                           │
                    User Question
                           │
                           ▼
                  ┌──────────────────┐
                  │ Query Processing │
                  └────────┬─────────┘
                           │
                           ▼
                  ┌──────────────────┐
                  │ Retrieve Relevant│
                  │     Chunks       │
                  └────────┬─────────┘
                           │
                           ▼
                  ┌──────────────────┐
                  │ Context + Query  │
                  └────────┬─────────┘
                           │
                           ▼
                  ┌──────────────────┐
                  │  Google Gemini   │
                  │       LLM        │
                  └────────┬─────────┘
                           │
                           ▼
                  ┌──────────────────┐
                  │ AI Answer +      │
                  │ Source Reference │
                  └──────────────────┘
## 🔄 How RAG Works

The system works in two major stages.

### 1. Document Ingestion

```text
PDF
 ↓
Text Extraction
 ↓
Text Chunking
 ↓
Embedding Generation
 ↓
FAISS Vector Database
### 2. Question Answering
User Question
 ↓
Query Embedding
 ↓
FAISS Similarity Search
 ↓
Relevant Chunks
 ↓
Context + Question
 ↓
Google Gemini
 ↓
Final Answer
| Technology    | Purpose                         |
| ------------- | ------------------------------- |
| Python        | Main programming language       |
| Streamlit     | Web application interface       |
| LangChain     | RAG workflow                    |
| FAISS         | Vector database                 |
| Hugging Face  | Text embeddings                 |
| Google Gemini | Large Language Model            |
| PyPDF         | PDF text extraction             |
| python-dotenv | Environment variable management |
📁 Project Structure

rag-project/
│
├── app.py
├── ingest.py
├── test_gemini.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── vectorstore/
│   └── FAISS vector database
│
└── .env
📊 Project Workflow
                    ┌─────────────────┐
                    │      User       │
                    └────────┬────────┘
                             │
                             ▼
                  ┌─────────────────────┐
                  │ Streamlit Interface │
                  └──────────┬──────────┘
                             │
              ┌──────────────┴──────────────┐
              │                             │
              ▼                             ▼
       ┌─────────────┐              ┌────────────────┐
       │  Upload PDF │              │ Ask Question   │
       └──────┬──────┘              └───────┬────────┘
              │                             │
              ▼                             ▼
       ┌─────────────┐              ┌────────────────┐
       │PDF Processing│              │Similarity Search│
       └──────┬──────┘              └───────┬────────┘
              │                             │
              ▼                             ▼
       ┌─────────────┐              ┌────────────────┐
       │Text Chunking│              │Relevant Context│
       └──────┬──────┘              └───────┬────────┘
              │                             │
              ▼                             ▼
       ┌─────────────┐              ┌────────────────┐
       │  Embeddings │              │   Gemini LLM   │
       └──────┬──────┘              └───────┬────────┘
              │                             │
              ▼                             ▼
       ┌─────────────┐              ┌────────────────┐
       │    FAISS    │─────────────▶│Generated Answer│
       └─────────────┘              └───────┬────────┘
                                            │
                                            ▼
                                    ┌────────────────┐
                                    │      User      │
                                    └────────────────┘
