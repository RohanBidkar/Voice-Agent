from typing import TypedDict

class CallState(TypedDict):
    call_sid: str
    caller_number: str
    recording_url: str
    transcript: str
    summary: str
