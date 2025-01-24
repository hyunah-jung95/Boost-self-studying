from langchain_google_vertexai import ChatVertexAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.messages import HumanMessage

def answer(docs):
    llm = ChatVertexAI(model="gemini-1.5-flash")
    question_answering_prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "You are an assistant specialized in simplifying technical concepts for software engineers. Your role is to explain the provided topic clearly, using code examples where necessary. Ensure your responses are concise, approachable, and focus on teaching the foundational understanding of the topic. {context}",
            ),
            MessagesPlaceholder(variable_name="messages")
        ]
    )
    document_chain = create_stuff_documents_chain(llm, question_answering_prompt)
    answer = document_chain.invoke(
        {
            "context": docs,
            "messages": [
                HumanMessage(content="Explain about the topics for someone professional on topic. Please include examples to make it more practical.")
            ],
        }
    )
    return answer