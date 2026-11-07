"""we will split the documents into chunks using the text splitter. The text splitter will split the documents into chunks based on the chunk size and the chunk overlap. The chunk size and the chunk overlap will be passed as arguments to the text splitter. The text splitter will return a list of chunks. Each chunk will be a document object with the page content and metadata. The page content will be the text of the chunk and the metadata will be the metadata of the original document."""

from langchain_text_splitters import RecursiveCharacterTextSplitter
from hr_assistant import config

def split_into_chunks(documents, chunk_size= config.CHUNK_SIZE, chunk_overlap=config.CHUNK_SIZE):
    """splits the documents into chunks using the text splitter. The text splitter will split the documents into chunks based on the chunk size and the chunk overlap. The chunk size and the chunk overlap will be passed as arguments to the text splitter. The text splitter will return a list of chunks. Each chunk will be a document object with the page content and metadata. The page content will be the text of the chunk and the metadata will be the metadata of the original document""".
     
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size, 
        chunk_overlap=chunk_overlap,
        #separators=["\n\n", "\n", " ", ""],
        )
    return text_splitter.split_documents(documents)
print("Text Splitter: Documents have been split into chunks successfully and number of chunks created is: ", len(split_into_chunks))