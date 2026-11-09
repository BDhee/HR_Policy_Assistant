"All settings for APp live, are found here. This file is used to store all the settings for the application. " 

import os
from dotenv import load_dotenv

load_dotenv()

## ENV vareiables 

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
JINA_API_KEY = os.getenv("JINA_API_KEY")

# GATEWAY 

PORTKEY_API_KEY = os.getenv("PORTKEY_API_KEY")

# GUARD MODEL 

GUARD_MODEL_NAME = "openai/gpt-oss-safeguard-20b"

# TRACING 

LANGSMITH_TRACING = os.getenv("LANGSMITH_TRACING", "false")
LANGSMITH_ENDPOINT = os.getenv("LANGSMITH_ENDPOINT")
LANGSMITH_API_KEY = os.getenv("LANGSMITH_API_KEY")
LANGSMITH_PROJECT = os.getenv("LANGSMITH_PROJECT")



#File Path for the data to be stored in the local storage.

DATA_FILE_PATH = os.path.join ("data", "hr_policy.txt")

#Vector store path 
VECTOR_STORE_PATH = os.path.join("data", "faiss_index")

##Memory 

#in memory, persistent memory or cloud memory( here we will be using persistant memory)

##Model settings

LLM_MODEL_NAME = "openai/gpt-oss-120b"

##embeddings model settings, we can use any of the open source models or paid models. Here we will be using paid model from OpenAI.

EMBEDDINGS_MODEL_NAME = "jina-embeddings-v2-base-es"

##text splitter settings.

CHUNK_SIZE = 1000
CHUNK_OVERLAP = 100

# RETRIEVER RESULTS

TOP_K-RESULTS = 3

#SYSTEM PROMPT

SYSTEM_PROMPT = (
    "You are a friendly HR assistant. Always use the search_hr_policy tool to look up "
    "facts before answering. If the answer isn't in the search results, say you don't know "
    "instead of guessing."
)

def check_api_key()-> str:
    """checks if the API key is available, if not it throws an error
    """
    if not GROQ_API_KEY:
        return(f"Error: GROQ_API_KEY is not set. Please set it in your environment file.")
    if not JINA_API_KEY:
        return(f"Error: JINA_API_KEY is not set. Please set it in your environment file.")
    if not QDRANT_URL or not QDRANT_API_KEY:
        raise ValueError("Missing QDRANT_URL/QDRANT_API_KEY. Please add them to your .env file.")
    if not PORTKEY_API_KEY:
        raise ValueError("Missing PORTKEY_API_KEY. Please add it to your .env file.")
    