from langchain_community.chat_models import ChatOllama
from typing import TypedDict

ollama_agent = ChatOllama(
    model="gpt-oss:20b",
    base_url="http://10.1.1.59:11434"
)


class State(TypedDict):
    query: str
    research: str
    summary: str
# Agent A: Research Agent
def research_node(state: State):
    print("-----------research node-----------------")
    q = state["query"]
    res = ollama_agent.invoke(f"Explain information about the following topic: {q}")
    state["research"] = res.content
    print(res.content)
    return state

# Agent B: Summarizer Agent
def summary_node(state: State):
    print("-----------summary node-----------------")
    text = state["research"]
    res = ollama_agent.invoke(f"Use Traditional Chinese. Summarize the following content into three key points: {text}")
    state["summary"] = res.content
    print(res.content)
    return state


from langgraph.graph import StateGraph, END

graph = StateGraph(State)

graph.add_node("ResearchAgent", research_node)
graph.add_node("SummarizerAgent", summary_node)

graph.set_entry_point("ResearchAgent")
graph.add_edge("ResearchAgent", "SummarizerAgent")
graph.add_edge("SummarizerAgent", END)

app = graph.compile()

resp = app.invoke({"query": "Ollama"})

print("-----------result-----------------")
print(resp["summary"])

