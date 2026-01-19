from langchain_openai import ChatOpenAI
import os

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
llm = ChatOpenAI()
print(llm)