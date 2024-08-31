import os
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import create_retrieval_chain
from langchain.schema import HumanMessage

from dotenv import load_dotenv
load_dotenv()

# Load the Groq API key
groq_api_key = os.environ['GROQ_API_KEY']

# Initialize the language model
llm = ChatGroq(model="Llama-3.1-70b-Versatile", temperature=0.0)

# Define the text to be replied to
text = "Hello"
prompt = f"Give a pleasant reply to: {text}"

# Generate a response
answer = llm([HumanMessage(content=prompt)])

# Output the answer (for demonstration purposes)
print(answer.content)
def respond(text):
    prompt = f"Give a pleasant reply to: {text}"

    # Generate a response
    answer = llm([HumanMessage(content=prompt)])
    return answer.content
