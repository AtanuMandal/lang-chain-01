from pathlib import Path
from dotenv import dotenv_values
from data_ingest import load_data, load_pdf, load_web_page


def main():
    
    env_path = Path(__file__).parent / ".env"
    if env_path.exists():
        vals = dotenv_values(env_path)

    value = vals.get("OPENAI_API_KEY", "Not Found") if vals else "Not Found"
    print(f"OPENAI_API_KEY: {value}")
    # Example usage of text loader
    file_path = Path(__file__).parent / "docs/linkedin.txt"
    if file_path.exists():
        documents = load_data(file_path)
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
    for doc in documents:
        print(doc.page_content[:500])  # Print first 500 characters
        print("----------------------------------   ----------------")
    print(f"Loaded {len(documents)} documents from {url}")


if __name__ == "__main__":
    main()

