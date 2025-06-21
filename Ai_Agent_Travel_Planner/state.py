from typing import TypedDict, List
from langchain_core.messages import BaseMessage

class TravelState(TypedDict):
    messages: List[BaseMessage]
