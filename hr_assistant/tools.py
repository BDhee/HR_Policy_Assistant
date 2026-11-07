"""wrap the retriever as the tool to the agent"""

from langchain.tools import Tool
from hr_assistant import config


def create_searech_tool(retriver):
    """returns a @tool function that reads the HR policy document"""

    @tool
    def search_hr_policy(query: str) -> str:
        """search the HR policy documents about the leave policy and
          work from home and relevent information in the doucment
        """

        matching_chunks= retriver.invoke(question)
        return "/n/n".join([chunk.page_content for chunk in matching_chunks])

    return search_hr_policy        


