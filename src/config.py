import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()
os.environ["SERPER_API_KEY"] = os.getenv("SERPER_API_KEY")
LLM = ChatGroq(model="llama3-8b-8192", temperature=0.7)