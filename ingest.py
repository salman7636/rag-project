from pypdf import PdfReader

from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

from langchain_text_splitters import RecursiveCharacterTextSplitter


# ============================================================
# EXTRACT PAGES FROM PDF
# ============================================================

def extract_pages_from_pdf(pdf_file):

    reader = PdfReader(pdf_file)

    pages = []

    for page_number, page in enumerate(
        reader.pages,
        start=1
    ):

        text = page.extract_text()

        if text and text.strip():

            pages.append({
                "page": page_number,
                "text": text.strip()
            })

    return pages


# ============================================================
# SPLIT PAGES INTO CHUNKS
# ============================================================

def split_pages(
    pages,
    chunk_size=1000,
    chunk_overlap=200
):

    documents = []

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        separators=[
            "\n\n",
            "\n",
            ". ",
            " ",
            ""
        ]
    )

    for page in pages:

        chunks = splitter.split_text(
            page["text"]
        )

        for chunk in chunks:

            if chunk.strip():

                documents.append({
                    "text": chunk.strip(),
                    "page": page["page"]
                })

    return documents


# ============================================================
# CREATE FAISS VECTOR DATABASE
# ============================================================

def create_vector_database(documents):

    embeddings = HuggingFaceEmbeddings(
        model_name=(
            "sentence-transformers/"
            "all-MiniLM-L6-v2"
        )
    )

    texts = [
        document["text"]
        for document in documents
    ]

    metadatas = [
        {
            "page": document["page"],
            "source": document.get(
                "source",
                "Unknown"
            )
        }
        for document in documents
    ]

    vector_database = FAISS.from_texts(
        texts,
        embedding=embeddings,
        metadatas=metadatas
    )

    return vector_database


# ============================================================
# SAVE VECTOR DATABASE
# ============================================================

def save_vector_database(
    vector_database,
    folder_path="vectorstore"
):

    import os

    # Create folder if it doesn't exist
    os.makedirs(
        folder_path,
        exist_ok=True
    )

    # Save FAISS database
    vector_database.save_local(
        folder_path
    )


# ============================================================
# LOAD VECTOR DATABASE
# ============================================================

def load_vector_database(
    folder_path="vectorstore"
):

    import os

    # Check whether vectorstore exists
    if not os.path.exists(folder_path):

        return None

    # Create the same embedding model
    embeddings = HuggingFaceEmbeddings(
        model_name=(
            "sentence-transformers/"
            "all-MiniLM-L6-v2"
        )
    )

    # Load FAISS database
    vector_database = FAISS.load_local(
        folder_path,
        embeddings,
        allow_dangerous_deserialization=True
    )

    return vector_database