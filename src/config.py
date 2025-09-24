import os
from dotenv import load_dotenv
from crewai import LLM

load_dotenv()
os.environ["SERPER_API_KEY"] = os.getenv("SERPER_API_KEY")
LLM = LLM(model="gemini/gemini-1.5-flash", temperature=0.7, api_key=os.getenv("GOOGLE_API_KEY"))