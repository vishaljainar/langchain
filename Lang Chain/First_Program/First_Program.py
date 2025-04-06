import os
import dotenv

from langchain.llms import  openai
from langchain.agents import load_tools, initialize_agent, AgentType

dotenv.load_dotenv()

# llm = OpenAI(temperature=0)
llm = AzureOpenAI(temperature=0)

tools = load_tools(["serpapi", "llm-math"], llm=llm)

agent = initialize_agent(
    tools,
    llm,
    agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

agent.run("Halve the current temperature in New York City and then add 1")
