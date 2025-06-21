from langgraph.graph import StateGraph
from langgraph.prebuilt import ToolNode, tools_condition
from langgraph.checkpoint.memory import MemorySaver
from agent.planner_agent import agent_llm, tools
from langgraph.graph import StateGraph,MessagesState,START,END
def create_workflow():
    graph = StateGraph(MessagesState)
    graph.add_node("llm_decision_step", agent_llm)
    graph.add_node("tools", ToolNode(tools))
    graph.add_edge("__start__", "llm_decision_step")
    graph.add_conditional_edges("llm_decision_step", tools_condition)
    graph.add_edge("tools", "llm_decision_step")
    memory=MemorySaver()
    return graph.compile(checkpointer=memory)
