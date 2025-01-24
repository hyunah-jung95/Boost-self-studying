from langchain.storage import LocalFileStore
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_google_vertexai import VertexAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.embeddings import CacheBackedEmbeddings
from langchain_community.cache import SQLiteCache
from langchain_core.globals import set_llm_cache
import streamlit as st

def embed_file(file):
    set_llm_cache(SQLiteCache(database_path=".cache/chats/langchain.db"))
    file_content = file.read()
    file_path = f"./.cache/files/{file.name}"
    with open(file_path, "wb") as f:
        f.write(file_content)
    loader = PyPDFLoader(file_path)

    pages = []
    for page in loader.lazy_load():
        pages.append(page)

    st.write("loading pages...")

    # Split
    text_splitter = CharacterTextSplitter.from_tiktoken_encoder(
        encoding_name="cl100k_base", separator="\n", chunk_size=200, chunk_overlap=100
    )
    texts = loader.load_and_split(text_splitter=text_splitter)

    st.write("Splitting docs...")

    # Embed
    embeddings_model = VertexAIEmbeddings(model="text-embedding-004")
    cache_dir = LocalFileStore("./.cache/embeddings/{file.name}")
    cached_embeddings = CacheBackedEmbeddings.from_bytes_store(embeddings_model, cache_dir)
    vectorstore = FAISS.from_documents(texts, cached_embeddings)
    retriever = vectorstore.as_retriever()
    st.write("Embedding data...")
    
    return retriever
