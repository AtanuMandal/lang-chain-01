import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.agents import create_agent

load_dotenv()

def get_weather(city : str):
    '''
    Docstring for get_weather
    '''
    return f"its nice and cool weather here @ {city}"

agent = create_agent(model="gpt-4.1", tools=[get_weather],system_prompt="you are an useful assistant")

response = agent.invoke( {"messages": [{"role": "user", "content": "what is the weather in Kolkata"}]})

print(response)