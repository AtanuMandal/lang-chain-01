from langchain_huggingface.embeddings import HuggingFaceEmbeddings

def hf_embed_query(text):
    
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")
    qtext = "This is a test document."
    query_result = embeddings.embed_query(text)
    print(query_result[:3])

def hf_embed_doc(text):
    
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")
    doc_result = embeddings.embed_documents([text])
    print(doc_result)