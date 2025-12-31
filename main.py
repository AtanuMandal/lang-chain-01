from pathlib import Path
from dotenv import load_dotenv
from data_ingest import load_data, load_pdf, load_web_page
from text_splitter import split_text
from hugging_face import hf_embed_doc
import os


def main():
    # Example usage of text loader
    file_path = Path(__file__).parent / "docs/linkedin.txt"
    if file_path.exists():
        documents = load_data(file_path) 
        for doc in documents:
             split_helper(doc.page_content)
        print(f"Loaded {len(documents)} documents from {file_path}")

    # Example usage of pdf loader
    file_path = Path(__file__).parent / "docs/doc1.pdf"
    if file_path.exists():
        documents = load_pdf(file_path)
        # for doc in documents:
        #     print(doc.page_content)
        print(f"Loaded {len(documents)} documents from {file_path}")

    # Example usage of web page loader
    url = "https://lilianweng.github.io/posts/2023-06-23-agent/"
    documents = load_web_page(url)
    # for doc in documents:
    #     print(doc.page_content[:500])  # Print first 500 characters
    #     print("----------------------------------   ----------------")
    print(f"Loaded {len(documents)} documents from {url}")


def split_helper(text):
    chunks = split_text(text)
    for index,chunk in enumerate(chunks):
        print(index)
        hf_embedding(chunk)
    

def hf_embedding(text):
    load_dotenv()
    os.environ["HF_TOKEN"] = os.getenv("HF_TOKEN")
    hf_embed_doc(text)

if __name__ == "__main__":
    main()

