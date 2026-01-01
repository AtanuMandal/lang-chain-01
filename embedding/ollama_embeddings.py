from pathlib import Path

from langchain_ollama import OllamaEmbeddings
from langchain_core.vectorstores import InMemoryVectorStore

from data_ingest import load_data
from text_splitter import split_text


# -------------------------------------------------------------------
# Configuration
# -------------------------------------------------------------------

# Path to the source document(s)
FILE_PATH = Path(__file__).parent.parent / "docs/linkedin.txt"

# Initialize the embedding model
embeddings = OllamaEmbeddings(
    model="embeddinggemma",
)

# -------------------------------------------------------------------
# Load and preprocess documents
# -------------------------------------------------------------------

# Load documents from disk (returns LangChain Document objects)
documents = load_data(FILE_PATH)

# Split all documents into chunks
all_chunks: list[str] = []
for doc in documents:
    chunks = split_text(doc.page_content)
    all_chunks.extend(chunks)

# -------------------------------------------------------------------
# Create an in-memory vector store
# -------------------------------------------------------------------

# Build the vector store from all text chunks
vectorstore = InMemoryVectorStore.from_texts(
    texts=all_chunks,
    embedding=embeddings,
)

# -------------------------------------------------------------------
# Retrieval
# -------------------------------------------------------------------

# Convert the vector store into a retriever
retriever = vectorstore.as_retriever()

# Query the vector store for semantically similar chunks
query = "When was LCEL first thought of?"
retrieved_documents = retriever.invoke(query)

# -------------------------------------------------------------------
# Output
# -------------------------------------------------------------------

print(f"Retrieved {len(retrieved_documents)} document(s)\n")

# Print the most relevant result
if retrieved_documents:
    print("Top result:\n")
    print(retrieved_documents[0].page_content)
