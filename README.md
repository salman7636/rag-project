# 🤖 RAG Document AI

> An AI-powered document assistant that allows users to upload PDF documents, ask questions, generate summaries, and retrieve answers from their own documents using Retrieval-Augmented Generation (RAG).

---

## 📌 Project Overview

**RAG Document AI** is an intelligent document question-answering application built using Python, Streamlit, LangChain, FAISS, Hugging Face embeddings, and Google Gemini.

The application allows users to upload one or more PDF documents and interact with them using natural language.

Instead of relying only on the general knowledge of an AI model, the application first searches the uploaded documents for relevant information and then provides that information to the Gemini model to generate a context-aware response.

### Main Workflow

```text
PDF Document
     ↓
Text Extraction
     ↓
Text Chunking
     ↓
Embedding Generation
     ↓
FAISS Vector Database
     ↓
User Question
     ↓
Similarity Search
     ↓
Relevant Document Chunks
     ↓
Context + Question
     ↓
Google Gemini
     ↓
AI Generated Answer
     ↓
Source References
🎯 Objectives

The main objectives of this project are:

Build a practical Retrieval-Augmented Generation application.
Allow users to interact with their own PDF documents.
Extract useful information from uploaded documents.
Convert document content into searchable vector representations.
Retrieve relevant information using FAISS similarity search.
Generate context-aware answers using Google Gemini.
Provide document summarization functionality.
Display relevant sources and page information.
Create a simple and user-friendly web interface.
Deploy the application using Streamlit.
✨ Features
📄 PDF Upload

Users can upload one or multiple PDF documents through the Streamlit interface.

🔍 Text Extraction

The application extracts text from uploaded PDF files.

✂️ Text Chunking

Large documents are divided into smaller chunks so that relevant information can be retrieved efficiently.

🧠 Embeddings

The application converts text chunks into numerical vector representations using embedding models.

🗃️ FAISS Vector Database

The generated embeddings are stored in FAISS for fast similarity-based retrieval.

💬 Document Question Answering

Users can ask questions about their uploaded documents.

Example:

What is the main topic of this document?
🤖 Google Gemini

Relevant document information is provided to Google Gemini to generate the final answer.

📝 Document Summarization

The application can generate summaries of uploaded documents.

📚 Source References

The application can display relevant document sources and page information.

🌐 Web Interface

The project uses Streamlit to provide an interactive web-based interface.

🔐 Secure API Key Management

API keys are loaded using environment variables locally and Streamlit Secrets during deployment.

🏗️ System Architecture
                         ┌──────────────────────┐
                         │        USER          │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │ Streamlit Interface  │
                         │       app.py         │
                         └──────────┬───────────┘
                                    │
                     ┌──────────────┴──────────────┐
                     │                             │
                     ▼                             ▼
              ┌──────────────┐             ┌───────────────┐
              │  Upload PDF  │             │ Ask Question  │
              └──────┬───────┘             └───────┬───────┘
                     │                             │
                     ▼                             ▼
              ┌──────────────┐             ┌───────────────┐
              │Text Extraction│             │Query Processing│
              └──────┬───────┘             └───────┬───────┘
                     │                             │
                     ▼                             ▼
              ┌──────────────┐             ┌───────────────┐
              │Text Chunking │             │Similarity Search│
              └──────┬───────┘             └───────┬───────┘
                     │                             │
                     ▼                             ▼
              ┌──────────────┐             ┌───────────────┐
              │  Embeddings  │             │Relevant Chunks│
              └──────┬───────┘             └───────┬───────┘
                     │                             │
                     ▼                             ▼
              ┌──────────────┐             ┌───────────────┐
              │FAISS Vector  │────────────▶│Context + Query│
              │    Store     │             └───────┬───────┘
              └──────────────┘                     │
                                                   ▼
                                            ┌───────────────┐
                                            │ Google Gemini │
                                            │      LLM      │
                                            └───────┬───────┘
                                                    │
                                                    ▼
                                            ┌───────────────┐
                                            │Generated Answer│
                                            └───────┬───────┘
                                                    │
                                                    ▼
                                            ┌───────────────┐
                                            │     USER      │
                                            └───────────────┘
🔄 How RAG Works

RAG stands for:

Retrieval-Augmented Generation

The system works mainly in two stages.

1️⃣ Document Ingestion

When the user uploads a PDF, the document goes through the following process:

PDF
 ↓
Text Extraction
 ↓
Text Chunking
 ↓
Embedding Generation
 ↓
FAISS Vector Database
Step 1: PDF Upload

The user uploads a PDF through the Streamlit interface.

Step 2: Text Extraction

Text is extracted from the uploaded document.

Step 3: Text Chunking

The extracted text is divided into smaller chunks.

This makes it easier to search for specific information.

Step 4: Embedding Generation

Each text chunk is converted into a numerical vector representation.

Step 5: FAISS Storage

The generated embeddings are stored in a FAISS vector database.

2️⃣ Question Answering

When the user asks a question:

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
Step 1: User Question

The user asks a question about the uploaded document.

Example:

What are the main conclusions of this document?
Step 2: Query Processing

The question is converted into a searchable representation.

Step 3: Similarity Search

FAISS searches the vector database for the most relevant document chunks.

Step 4: Context Retrieval

The relevant chunks are selected as context.

Step 5: Gemini

The retrieved context and user question are provided to Google Gemini.

Step 6: Final Answer

Gemini generates an answer based on the retrieved document information.

🛠️ Technologies Used
Technology	Purpose
Python	Main programming language
Streamlit	Web application interface
LangChain	RAG and LLM workflow
FAISS	Vector similarity search
Hugging Face	Text embeddings
Google Gemini	Large Language Model
PyPDF	PDF text extraction
python-dotenv	Environment variable management
Git	Version control
GitHub	Source code hosting
📁 Project Structure
rag-project/
│
├── app.py
│
├── ingest.py
│
├── test_gemini.py
│
├── requirements.txt
│
├── README.md
│
├── .gitignore
│
├── vectorstore/
│   └── FAISS vector database
│
└── .env
File Description
File / Folder	Description
app.py	Main Streamlit application
ingest.py	Document ingestion and processing
test_gemini.py	Gemini API testing
requirements.txt	Python dependencies
vectorstore/	Vector database storage
.gitignore	Prevents sensitive/unwanted files from Git
.env	Stores local API credentials
README.md	Project documentation
⚙️ Installation
1. Clone the Repository
git clone https://github.com/salman7636/rag-project.git
2. Open the Project Directory
cd rag-project
3. Create a Virtual Environment

For Windows:

python -m venv venv
4. Activate the Virtual Environment

For Windows PowerShell:

.\venv\Scripts\Activate.ps1

After activation, you should see:

(venv)

at the beginning of the terminal.

5. Install Dependencies
pip install -r requirements.txt
🔑 API Key Configuration

The application requires a Google Gemini API key.

Create a file named:

.env

in the project root directory.

Add:

GOOGLE_API_KEY=YOUR_GEMINI_API_KEY

Replace:

YOUR_GEMINI_API_KEY

with your actual API key.

⚠️ Security Warning

Never upload your actual .env file to GitHub.

Make sure .env is included in .gitignore.

Example:

.env
venv/
__pycache__/
▶️ Running the Application

After installing all dependencies and configuring the API key, run:

streamlit run app.py

Alternatively:

python -m streamlit run app.py

The application will normally open at:

http://localhost:8501
💻 Using the Application
Step 1 — Open the Application

Run:

streamlit run app.py

Then open:

http://localhost:8501
Step 2 — Upload PDF

Upload one or more PDF documents.

Example:

📄 research-paper.pdf
📄 operating-system-notes.pdf
Step 3 — Process Documents

Click:

🚀 Process & Index PDFs

The application processes the documents.

The workflow is:

PDF
 ↓
Text Extraction
 ↓
Text Chunking
 ↓
Embeddings
 ↓
FAISS
Step 4 — Ask a Question

After processing, ask a question.

Example:

What is the main topic of this document?

Other examples:

What are the important points?


Explain the conclusion.


What methodology was used?


Give me a short summary.


What are the key findings?
Step 5 — Retrieve the Answer

The system searches the FAISS vector database and retrieves relevant information.

Gemini then generates the final answer.

📝 Document Summarization

The application can also generate a summary of the selected document.

A summary can help users quickly understand the main points without reading the complete document.

📚 Source Retrieval

The application can provide relevant source information along with generated answers.

This helps users understand where the retrieved information came from.

🔐 Security

Security is an important part of the project.

The project follows these practices:

API keys are not stored directly inside the application code.
.env is used for local development.
.env is excluded from GitHub using .gitignore.
Streamlit Secrets are used for deployment.
API keys should never be committed to GitHub.
If an API key is accidentally exposed, it should be revoked immediately.
A new API key should then be generated.
🌐 Streamlit Deployment

The application can be deployed using Streamlit Community Cloud.

Deployment Configuration
Repository:
salman7636/rag-project


Branch:
main


Main file:
app.py


Python version:
3.12
Streamlit Secrets

Instead of using .env on Streamlit Cloud, add the API key under Secrets.

Use:

GOOGLE_API_KEY = "YOUR_GEMINI_API_KEY"

Do not put the real API key inside:

app.py

or:

README.md
🏠 Localhost vs Cloud Deployment
Localhost

When running:

streamlit run app.py

the application runs on your own computer.

The normal address is:

http://localhost:8501

Only your local environment can normally access it.

Cloud Deployment

After deploying the application to Streamlit Cloud, it receives a public web address.

Users can then access the application through their browser.

Localhost
    ↓
Your Computer
    ↓
Streamlit Application

Whereas:

Internet
    ↓
Streamlit Cloud
    ↓
RAG Document AI
📊 Complete Project Workflow
                         USER
                           │
                           ▼
                ┌────────────────────┐
                │ Streamlit Frontend │
                └──────────┬─────────┘
                           │
             ┌─────────────┴─────────────┐
             │                           │
             ▼                           ▼
      Upload PDF                    Ask Question
             │                           │
             ▼                           ▼
      Text Extraction              Query Processing
             │                           │
             ▼                           ▼
       Text Chunking              Query Embedding
             │                           │
             ▼                           ▼
        Embeddings                FAISS Search
             │                           │
             ▼                           ▼
           FAISS                Relevant Chunks
             │                           │
             └─────────────┬─────────────┘
                           │
                           ▼
                   Context + Question
                           │
                           ▼
                    Google Gemini
                           │
                           ▼
                    AI Generated
                       Answer
                           │
                           ▼
                       Sources
                           │
                           ▼
                          USER
🧠 RAG Pipeline

The complete RAG pipeline can be summarized as:

1. Upload Document
        ↓
2. Extract Text
        ↓
3. Split Text
        ↓
4. Generate Embeddings
        ↓
5. Store in FAISS
        ↓
6. Receive User Question
        ↓
7. Search FAISS
        ↓
8. Retrieve Relevant Chunks
        ↓
9. Combine Context + Question
        ↓
10. Send to Gemini
        ↓
11. Generate Answer
        ↓
12. Display Answer + Sources
🎯 Advantages

The RAG approach provides several advantages:

📚 Document-Specific Answers

The application can answer questions based on the user's uploaded documents.

🔎 Efficient Retrieval

FAISS allows efficient similarity-based retrieval of relevant information.

🤖 AI-Powered Responses

Google Gemini generates natural-language answers.

💬 Natural Interaction

Users can ask questions using normal language.

📄 Multiple Documents

Users can work with multiple PDF documents.

🔐 Private Local Processing

When running locally, documents can be processed on the user's own machine.

⚠️ Limitations

The current version may have limitations such as:

PDF-only document support.
Answer quality depends on the quality of retrieved chunks.
Scanned/image-only PDFs may require OCR.
Large documents may require more processing time.
Gemini API usage may be subject to API limits.
Vector database persistence depends on the application configuration.
Internet connectivity may be required for Gemini API calls.
🔮 Future Improvements

Possible future improvements include:

🔐 User authentication
📚 DOCX support
📝 TXT support
📊 CSV support
🖼️ Image and scanned PDF support
🔎 Advanced search filters
💬 Conversation history
👤 User-specific document collections
🗂️ Document management
🎙️ Voice-based questions
🌍 Multi-language support
☁️ Cloud vector database
⚡ Streaming responses
📈 Analytics dashboard
🔔 Notification system
🧠 Improved retrieval techniques
🔐 Advanced security
📱 Mobile-friendly interface
🧪 Example Questions

Users can ask questions such as:

What is this document about?
Give me a summary of this document.
What are the main objectives?
Explain the methodology.
What are the key findings?
What are the conclusions?
List the important points from the document.
Explain this topic in simple words.
🖥️ Application Interface

The application contains:

┌──────────────────────────────────────────┐
│          🤖 RAG Document AI              │
│                                          │
│   Upload • Search • Ask • Summarize      │
├──────────────────────────────────────────┤
│                                          │
│          📄 Upload PDF                   │
│                                          │
│       [ Choose PDF files ]               │
│                                          │
│       🚀 Process & Index PDFs             │
│                                          │
├──────────────────────────────────────────┤
│                                          │
│          📚 Document Tools               │
│                                          │
│          📝 Summary                      │
│                                          │
│          💬 Ask AI                       │
│                                          │
└──────────────────────────────────────────┘
📌 Project Use Cases

This project can be useful for:

📚 Students studying from notes
🔬 Researchers analyzing papers
🏢 Organizations working with documents
📑 Legal document analysis
🏥 Healthcare document analysis
📖 Academic research
📋 Business reports
📊 Technical documentation
🧑‍💻 Developers working with technical PDFs
🎓 Educational Value

This project demonstrates practical knowledge of:

Python programming
Generative AI
Large Language Models
Retrieval-Augmented Generation
Natural Language Processing
Vector databases
Semantic search
Embeddings
LangChain
FAISS
Streamlit
API integration
Environment variable management
Git and GitHub
Cloud deployment
🧩 Key Components
Frontend
Streamlit

Provides the user interface for:

PDF upload
Document processing
Chat
Summary
Source display
Document Processing
PyPDF / PDF Loader

Responsible for extracting text from PDF documents.

Text Splitting
Recursive Character Text Splitter

Divides large documents into smaller chunks.

Embeddings
Hugging Face Embeddings

Converts text into numerical vector representations.

Vector Database
FAISS

Stores and searches document embeddings.

Large Language Model
Google Gemini

Generates the final natural-language response.

📈 Why RAG Instead of Direct LLM?

A traditional LLM can answer questions using its pretrained knowledge.

However, it may not know the contents of a user's private PDF.

RAG solves this problem by retrieving relevant information from the user's documents first.

Traditional LLM


Question
   ↓
LLM
   ↓
Answer

RAG:

Question
   ↓
Retrieve Relevant Information
   ↓
Document Context
   ↓
Gemini
   ↓
Context-Aware Answer

This allows the application to work with information contained in user-provided documents.

🛠️ Troubleshooting
Problem: GOOGLE_API_KEY not configured

Make sure your .env contains:

GOOGLE_API_KEY=YOUR_GEMINI_API_KEY

For Streamlit Cloud, make sure the key is added under Secrets:

GOOGLE_API_KEY = "YOUR_GEMINI_API_KEY"
Problem: Streamlit command not found

Use:

python -m streamlit run app.py
Problem: Dependencies are missing

Run:

pip install -r requirements.txt
Problem: Virtual environment is not activated

Windows PowerShell:

.\venv\Scripts\Activate.ps1
📜 GitHub Commands

After making changes:

git status

Add changes:

git add .

Commit:

git commit -m "Update RAG Document AI"

Push:

git push origin main
👨‍💻 Author
Salman Firdous

Computer Science Engineering Student

GitHub:

https://github.com/salman7636

Project Repository:

https://github.com/salman7636/rag-project

⭐ Acknowledgements

This project was developed using the following technologies and tools:

Python
Streamlit
LangChain
FAISS
Hugging Face
Google Gemini
PyPDF
Git
GitHub
📄 License

This project is intended for educational, learning, and project-development purposes.

⭐ Support

If you find this project useful, consider giving the repository a ⭐ on GitHub.

🔒 Important Security Notice

Never expose your real API key.

Do NOT put your real key in:

app.py
README.md
GitHub
screenshots
LinkedIn posts

For local development:

GOOGLE_API_KEY=YOUR_GEMINI_API_KEY

For Streamlit Cloud:

GOOGLE_API_KEY = "YOUR_GEMINI_API_KEY"

Always use your actual key only in your local .env file or secure Streamlit Secrets.



Then your repository will have a proper **project overview + architecture + installation + usage + RA
