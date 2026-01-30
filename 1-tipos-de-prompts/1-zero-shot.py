import os
from langchain_xai import ChatXAI
from dotenv import load_dotenv
from utils import print_llm_result

load_dotenv()
msg1 = "What's Brazil's capital?"

msg2 = """
Find the user intent in the following text: 
I'm looking for a restaurant around São Paulo who has a good rating for Japanese food.
"""

msg3 = "What's Brazil's capital? Respond only with the city name."

llm = ChatXAI(model="grok-4-1-fast-non-reasoning", api_key=os.getenv("GROK_API_KEY"))

response = llm.invoke(msg1)
print_llm_result(msg1, response)

response = llm.invoke(msg2)
print_llm_result(msg2, response)

response = llm.invoke(msg3)
print_llm_result(msg3, response)