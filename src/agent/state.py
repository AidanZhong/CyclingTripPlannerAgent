# -*- coding: utf-8 -*-
"""
Created on 16/01/2026 22:25

@author: Aidan
@project: CyclingTripPlannerAgent
@filename: state
"""
from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional

from src.schemas.trip import TripPreferences, TripPlan


@dataclass
class Message:
    role: str
    content: str


@dataclass
class SessionState:
    preferences: TripPreferences = field(default_factory=TripPreferences)
    history: list[Message] = field(default_factory=list)
    last_plan: Optional[TripPlan] = None
    last_tool_results: dict = field(default_factory=dict)
    updated_at: datetime = field(default_factory=datetime.now)


SESSION_STORE: dict[str, "SessionState"] = {}  # temporary in-memory store


def get_or_create_state(session_id) -> SessionState:
    if session_id in SESSION_STORE:
        return SESSION_STORE[session_id]
    session_state = SessionState()
    session_state.updated_at = datetime.now()
    SESSION_STORE[session_id] = session_state
    return session_state


def append_history(state, role, content):
    msg = Message(role=role, content=content)
    state.history.append(msg)
