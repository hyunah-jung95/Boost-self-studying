import streamlit as st

from processor.embedding import embed_file
from processor.answering import answer
from processor.wiki import wiki


st.title("Boosting Self-Studying")
st.subheader("Learn efficiently in easy way")

tab1, tab2 = st.tabs(["File", "Wikipedia"])

with tab1:
    file = st.file_uploader(
        "Upload pdf file",
        type=["pdf"],
    )
    button = st.button("Extract")

    if file and button:
        retriever = embed_file(file)
        docs = retriever.invoke("Retrieve a concise explanation of [technical topic] that is approachable for students who are learning this concept for the first time. Focus on clarity and avoid jargon, while retaining the key technical points.")
        st.write("Retriving...")
        st.divider()
        answer = answer(docs)
        st.write(answer)

with tab2:
    text = st.text_input("Ask to Wikipedia about any topic.")
    if text:
        docs = wiki(text)
        answer = answer(docs)
        st.write(answer)