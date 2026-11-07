"""This is the pipeline where all the functions are called in order to process the data. 
And this is the main file where the pipeline is executed.
And the entry point to the streamlit app. 
This file is responsible for executing the pipeline and generating the final output."""


from hr_assistant import config
from hr_assistant.agent import create_hr_agent
from hr_assistant.document_loaders import load_documents
from hr_assistant.llm import get_llm
from hr_assistant.splitter import split_into_chunks    
from hr_assistant.tools import create_searech_tool
from hr_assistant.vector_store import (build_vector_store, get_retriever ,  
                                        save_vector_store, load_vectore_store, vector_store_exists)


# data ingestion

def build_vector_store_for_document(file_path: str = config.DATA_FILE_PATH):
    """Load + split + embed the document, 
    reusing the Qdrant Cloud collection if we have one."""
    if vector_store_exists():
        print("Found an existing Qdrant Cloud collection, connecting to it (fast, no re-embedding).")
        logger.info("Qdrant Cloud collection already exists, reusing it")
        return load_vector_store()

    print("No Qdrant Cloud collection found, building one from scratch...")
    logger.info("No Qdrant Cloud collection found, building one from scratch")
    documents = load_document(file_path)
    chunks = split_into_chunks(documents)
    print(f"Loaded '{file_path}' and split it into {len(chunks)} chunks.")

    vector_store = build_vector_store(chunks)
    print("Vector store built and uploaded to Qdrant Cloud.")
    return vector_store


# data retreival    
    
def build_hr_assistant(file_path: str = config.DATA_FILE_PATH):
    """Build the full RAG agent, ready to answer questions."""
    logger.info("Building HR assistant...")
    config.check_api_keys()
    check_langsmith_tracing()

    vector_store = build_vector_store_for_document(file_path)
    retriever = get_retriever(vector_store)
    search_tool = create_search_tool(retriever)

    llm = get_llm()
    agent = create_hr_agent(llm, [search_tool])

    logger.info("HR assistant is ready to take questions")
    return agent


def ask(agent, question: str) -> str:
    """Ask the agent a question and
    return its final answer as plain text."""
    logger.info("User question: %s", question)
    
    # input guard - to get safe inputs 
    
    input_is_safe, _ = check_input(question)
    if not input_is_safe:
        return REFUSAL_MESSAGE
    
    response = agent.invoke({"messages": [{"role": "user", "content": question}]})
    answer = response["messages"][-1].content
    logger.info("Final answer: %s", answer)
    
    # output guard - to check if agent gives safe answer 
    output_is_safe, _ = check_output(answer)
    if not output_is_safe:
        return REFUSAL_MESSAGE