import os
from dotenv import load_dotenv
from langchain_ollama import ChatOllama

load_dotenv()
os.environ["SERPER_API_KEY"] = os.getenv("SERPER_API_KEY")
LLM = ChatOllama(model="ollama/deepseek-r1:7b", temperature=0.7)