from langgraph.graph import StateGraph, END
from app.agent.state import CallState
from app.agent.nodes import fetch_and_transcribe, summarize, notify


builder = StateGraph(CallState)

builder.add_node("transcribe", fetch_and_transcribe)
builder.add_node("summarize", summarize)
builder.add_node("notify", notify)

builder.set_entry_point("transcribe")
builder.add_edge("transcribe", "summarize")
builder.add_edge("summarize", "notify")
builder.add_edge("notify", END)

agent = builder.compile()


def run_agent(call_sid, caller_number, recording_url):
    agent.invoke({
        "call_sid": call_sid,
        "caller_number": caller_number,
        "recording_url": recording_url
    })
