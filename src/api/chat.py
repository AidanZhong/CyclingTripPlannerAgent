# -*- coding: utf-8 -*-
"""
Created on 15/01/2026 22:22

@author: Aidan
@project: CyclingTripPlannerAgent
@filename: chat
"""
from uuid import uuid4

from fastapi import APIRouter

from src.agent.orchestrator import handle_message
from src.schemas.api import ChatResponse, ChatRequest

router = APIRouter()


@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest) -> ChatResponse:
    session_id = request.session_id or str(uuid4())
    try:
        response = handle_message(session_id, request.message)
        return response
    except Exception as e:
        return ChatResponse(session_id=session_id, reply=str(e))
