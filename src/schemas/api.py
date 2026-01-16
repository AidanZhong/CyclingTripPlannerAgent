# -*- coding: utf-8 -*-
"""
Created on 16/01/2026 22:26

@author: Aidan
@project: CyclingTripPlannerAgent
@filename: api
"""


class ChatRequest:
    session_id: str
    message: str
    debug: bool = False


class ChatResponse:
    session_id: str
    reply: str
    debug_trace: DebugTrace | None


class DebugTrace:
    decisions: list[str]
    tools_called: list[ToolCallRecord]


class ToolCallRecord:
    tool_name: str
    tool_input: str
    tool_output: str
