# -*- coding: utf-8 -*-
"""
Created on 16/01/2026 22:26

@author: Aidan
@project: CyclingTripPlannerAgent
@filename: api
"""
from typing import Optional

from pydantic import BaseModel


class ChatRequest(BaseModel):
    session_id: Optional[str] = None
    message: str
    debug: bool = False


class ChatResponse(BaseModel):
    session_id: str
    reply: str
