""" this will generate the vector embeddings for the given text using embedding model"""
from langchain_community.embeddings import JinaEmbeddings
from hr_assistant import config


def get_embeddings_model():
    """generates the vector embeddings and reads the API key from the environment variable. The API key is used to authenticate the request to the embedding model. The embedding model is used to generate the vector embeddings for the given text. The vector embeddings are used to find the most similar documents to the given text."""
    return JinaEmbeddings(model_name= config.EMBEDDINGS_MODEL_NAME)
    #return embeddings.embed_query(text)

print("Embeddings: Vector embeddings have been generated successfully using the embedding model: ", config.EMBEDDINGS_MODEL_NAME)       