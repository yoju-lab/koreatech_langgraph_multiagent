from langchain_openai import ChatOpenAI
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from typing_extensions import TypedDict
from typing import Annotated, List
from dotenv import load_dotenv
import os

load_dotenv()
openai_model = os.getenv("OPENAI_MODEL", "gpt-4o-mini")

class State(TypedDict):
    messages: Annotated[List, add_messages]

llm = ChatOpenAI(model=openai_model)

def chatbot(state: State):
    response = llm.invoke(state["messages"])
    return {"messages": [response]}

workflow = StateGraph(State)
workflow.add_node("chatbot", chatbot)
workflow.add_edge(START, "chatbot")
workflow.add_edge("chatbot", END)
graph = workflow.compile()

from langchain_core.messages import HumanMessage
user_input = "LangGraph가 무엇인가요?"
state = {"messages": [HumanMessage(content=user_input)]}
response = graph.invoke(state)
print(response["messages"][-1].content)
