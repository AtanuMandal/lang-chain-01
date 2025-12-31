
# LangChain Tutorial — Document Loaders

This small tutorial demonstrates how to use document loaders with LangChain. The example code in this repository shows three loader types: text files, PDFs, and web pages.

**Files:**
- `main.py` — example runner that shows how to call the loaders and print results.
- `data_ingest.py` — contains the loader helper functions: `load_data()`, `load_pdf()`, and `load_web_page()`.

## Prerequisites
- Python 3.10+ recommended
- Create a virtual environment and activate it

## Installation
Install dependencies from `pyproject.toml` or with pip. Example using pip:

```bash
python -m venv .venv
.\.venv\Scripts\activate
pip install -U pip
pip install -r requirements.txt  # if you maintain one
```

If you're using the provided `pyproject.toml`, use your preferred tool (Poetry, pip with build isolation, etc.).

## Environment
If you want to test features that use an API key, create a `.env` file in the repository root with:

```
OPENAI_API_KEY=your_api_key_here
```

`main.py` reads `OPENAI_API_KEY` (if present) and demonstrates loader usage.

## Usage
Run the example script to exercise the loaders:

```bash
python main.py
```

The script will:
- Attempt to load `docs/linkedin.txt` using the text loader.
- Attempt to load `docs/doc1.pdf` using the PDF loader.
- Load the example web page via the web loader and print snippets.

Place any sample documents under the `docs/` folder (create it if missing).

## Loader details (see `data_ingest.py`)
- `load_data(file_path)` — uses a `TextLoader` to read plain text files.
- `load_pdf(file_path)` — uses `PyPDFLoader` to extract pages from PDFs.
- `load_web_page(url)` — uses `WebBaseLoader` with a BeautifulSoup `SoupStrainer` to parse selected page parts.

## Notes
- If you add large or sensitive files that should not be tracked, remove them from Git and add them to `.gitignore` (see `git rm --cached`).
- For production use, pin dependency versions and add tests.

## Next steps
- Add a `requirements.txt` or update `pyproject.toml` with exact versions.
- Add examples showing vectorization and querying loaded documents.

Happy experimenting!
