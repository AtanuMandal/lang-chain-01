from pinecone import Pinecone, ServerlessSpec
import os

pinecone_api_key = os.getenv("PINECONE_API_KEY")
pc = Pinecone(api_key=pinecone_api_key)