from langchain_community.document_loaders import TextLoader
from langchain_community.document_loaders import PyPDFLoader
import bs4
from langchain_community.document_loaders import WebBaseLoader

def load_data(file_path):
    loader = TextLoader(file_path)
    documents = loader.load()
    return documents

def load_pdf(file_path):
    loader = PyPDFLoader(file_path)
    documents = loader.load()
    return documents

def load_web_page(url):
    bs4_strainer = bs4.SoupStrainer(class_=("post-title", "post-header", "post-content"))
    loader = WebBaseLoader(web_paths=(url,),
    bs_kwargs={"parse_only": bs4_strainer},)
    documents = loader.load()
    return documents