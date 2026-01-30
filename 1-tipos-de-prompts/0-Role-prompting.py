import os
from langchain_xai import ChatXAI
from langchain_core.prompts import ChatPromptTemplate
from utils import print_llm_result
from dotenv import load_dotenv

load_dotenv()

system = ("system", 
"""You are a university professor of computer science who is very technical and explain 
concepts with formal definitions and pseudocode.""")

system2 =  ("system", """You are a high school student that is starting learning coding. 
You are not very technical and you prefer to explain concepts with simple words and examples.""")

user = ("user", "Explain recursion in 50 words.")

chat_prompt = ChatPromptTemplate([system, user])
chat_prompt2 = ChatPromptTemplate([system2, user])

messages = chat_prompt.format_messages()

model = ChatXAI(model="grok-4-1-fast-non-reasoning", api_key=os.getenv("GROK_API_KEY"))
response = model.invoke(messages)
print_llm_result(user[1], response)

messages2 = chat_prompt2.format_messages()
response2 = model.invoke(messages2)
print_llm_result(user[1], response2)