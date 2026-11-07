"""we will use the text loader to load the text data from the file and then we will use the text splitter to split the text into chunks. The chunks will be stored in a list and then we will use the list to create the vector store. The vector store will be used to store the embeddings of the chunks. The embeddings will be used to retrieve the relevant chunks based on the query. The retrieved chunks will be used to generate the answer to the query."""

from langchain_community.document_loaders import TextLoader
from hr_assistant import config


def load_documents(file_path: str = config.DATA_FILE_PATH):
    """returns the list of documents loaded from the file path. The file path is passed as an argument to the function. If the file path is not passed, it will use the default file path from the config file.

    Args:
        file_path (_type_, optional): _description_. Defaults to config.DATA_FILE_PATH.
    """
    loader = TextLoader(file_path, encoding="utf-8")
    return loader.load()

print("Document Loader: Documents have been loaded successfully from the file path: ", config.DATA_FILE_PATH)

      