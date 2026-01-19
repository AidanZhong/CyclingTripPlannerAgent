# -*- coding: utf-8 -*-
"""
Created on 15/01/2026 22:22

@author: Aidan
@project: CyclingTripPlannerAgent
@filename: chat
"""
from uuid import uuid4

from fastapi import APIRouter

from src.schemas.api import ChatResponse, ChatRequest

router = APIRouter()

@router.post("/chat", response_model=ChatResponse)
def chat(request:ChatRequest)->ChatResponse:
    session_id = request.session_id or str(uuid4())

    response = ChatResponse(session_id=session_id, reply=request.message)

    return response