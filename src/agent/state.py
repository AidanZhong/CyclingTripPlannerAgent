# -*- coding: utf-8 -*-
"""
Created on 16/01/2026 22:25

@author: Aidan
@project: CyclingTripPlannerAgent
@filename: state
"""
from datetime import datetime

from src.schemas.trip import TripPreferences, TripPlan


class Message:
    role: str
    content: str


class SessionState:
    preferences: TripPreferences
    history: list[Message]
    last_plan: TripPlan | None = None
    last_tool_results: dict
    updated_at: datetime


SESSION_STORE: dict[str, "SessionState"]  # temporary in-memory store


def get_or_create_state(session_id) -> SessionState:
    if session_id in SESSION_STORE:
        return SESSION_STORE[session_id]
    session_state = SessionState()
    session_state.updated_at = datetime.now()
    SESSION_STORE[session_id] = session_state
    return session_state


def append_history(state, role, content):
    msg = Message()
    msg.role = role
    msg.content = content
    SESSION_STORE[state].history.append(msg)
