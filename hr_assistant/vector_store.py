"""this stores the vector embeddings for the given text using embedding model"""

import os
from langchain.vectorstores import FAISS
from hr_assistant import config 
from hr_assistant.embeddings import get_embeddings_model

def build_vector_store(chunks):
    """ embeded every chunk and build a searchable FAISS index using the embeddings model
    """
    embeddings_model = get_embeddings_model()
    return FAISS.from_documents(chunks, embeddings_model)


## Save vector store locally
def save_vector_store(vector_store, path: str = config.VECTOR_STORE_PATH) -> None:
    """save the vector store locally to the given path. The vector store is saved in the local storage. The path is passed as an argument to the function. The default path is set to the VECTOR_STORE_PATH in the config.py file. 
    The vector store is saved in the local storage using the save_local method of the FAISS class.""" 
    vector_store.save_local(path)

def load_vectore_store(path:str = config.VECTOR_STORE_PATH):
    """load the vector store from the local storage. The vector store is loaded from the local storage using the load_local method of the FAISS class. The path is passed as an argument to the function. The default path is set to the VECTOR_STORE_PATH in the config.py file."""
    embeddings_model = get_embeddings_model()
    return FAISS.load_local(path, embeddings_model, allow_dangerous_deserialization=True)


def vector_store_exists(path:str = config.VECTOR_STORE_PATH) -> bool:
    """check if the vector store exists in the local storage. The vector store is checked in the local storage using the os.path.exists method. The path is passed as an argument to the function. The default path is set to the VECTOR_STORE_PATH in the config.py file."""
    return os.path.exists(os.join(path, "index,faiss"))

def get_retriever(vectore_store, k:int = config.top_k_results):
    """retrieve the vector store from the local storage. The vector store is retrieved from the local storage using the retrieve method of the FAISS class. The query is passed as an argument to the function. The top_k is passed as an argument to the function. The default top_k is set to the top_k_results in the config.py file."""
    return vectore_store.as_retriever(search_kwargs={"k": k})

