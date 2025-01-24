from langchain.retrievers import WikipediaRetriever

def wiki(topic):
    retriever = WikipediaRetriever(top_k_results=5)
    docs = retriever.get_relevant_documents(topic)
    return docs    