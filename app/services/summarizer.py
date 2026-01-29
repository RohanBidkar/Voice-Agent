from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
import os

def summarize_text(text: str) -> str:
    """Summarize text using Groq LLM"""
    llm = ChatGroq(
        model="llama-3.3-70b-versatile",
        temperature=0.2,
        api_key=os.getenv("GROQ_API_KEY")
    )
    
    prompt = ChatPromptTemplate.from_messages([
        ("system", 
         "You are an AI voicemail assistant. "
         "Summarize phone calls clearly and concisely."),
        ("human", "{text}")
    ])
    
    chain = prompt | llm
    result = chain.invoke({"text": text})
    return result.content
