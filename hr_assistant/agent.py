"""Step 7: Create the Agent"""

from langchain.agents import CreateAgent

from hr_assistant import config

def create_hr_agent(llm, tools):
    """returns the agent that reads the HR policy document and generates the response for the given query. The agent is created using the LLM model and the search tool. The search tool is used to search the HR policy documents and retrieve the relevant chunks. The retrieved chunks are used to generate the response for the given query."""
    return CreateAgent(model= llm,tools = tools,  
                           system_message = config.SYSTEM_MESSAGE,)