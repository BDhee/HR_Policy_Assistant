"""This file has the LLM model"""

from langchain_groq import ChatGroq   
from hr_assistant import config
def get_llm():
    """Returns the Groq models and reads the API  key from the environment variable. The API key is used to authenticate the request to the LLM model. The LLM model is used to generate the response for the given query. The response is generated using the LLM model and the search results from the vector store."""
    return ChatGroq(model_name=config.LLM_MODEL_NAME, temperature=0.5)
