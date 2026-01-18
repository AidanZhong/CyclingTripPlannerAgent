# -*- coding: utf-8 -*-
"""
Created on 16/01/2026 22:25

@author: Aidan
@project: CyclingTripPlannerAgent
@filename: orchestrator
"""
from copy import deepcopy

from src.agent.extractor import extract_route, extract_daily_distance, extract_month, extract_primary_accommodation, \
    extract_every_n_pattern
from src.agent.state import get_or_create_state, append_history
from src.schemas.api import ChatResponse
from src.schemas.trip import TripPreferences, AccommodationPreference
from src.utils.intent_matching import classify_message


def handle_message(session_id: str, message: str) -> ChatResponse:
    # get the state
    state = get_or_create_state(session_id)
    append_history(state, "user", message)

    # update the preferences
    old_preference = state.preferences
    new_preference = update_preferences_from_text(message, old_preference)
    state.preferences = new_preference

    # if missing some fields, ask for them
    missing = missing_fields(new_preference)
    if missing:
        # build a queue to ask
        q = build_question(missing)
        append_history(state, "assistant", q)
        return ChatResponse(
            session_id=session_id,
            reply=q
        )

    reply = "Great, I have everything I need to plan your trip!"
    append_history(state, "assistant", reply)
    return ChatResponse(
        session_id=session_id,
        reply=reply
    )

def update_preferences_from_text(text: str, old_preference: TripPreferences):
    intents = classify_message(...)
    p = deepcopy(old_preference)

    if "PROVIDE_ROUTE" in intents:
        origin, destination = extract_route(text)
        if origin:
            p.origin = origin
        if destination:
            p.destination = destination

    if "PROVIDE_DAILY_DISTANCE" in intents or "CHANGE_DAILY_DISTANCE" in intents:
        km = extract_daily_distance(text)
        if km:
            p.daily_distance_km = km

    if "PROVIDE_MONTH" in intents:
        mo = extract_month(text)
        if mo:
            p.start_month = mo

    if "PROVIDE_ACCOMMODATION_PRIMARY" in intents or "CHANGE_ACCOMMODATION" in intents:
        accommodation = extract_primary_accommodation(text)
        if accommodation:
            if p.accommodation is None:
                p.accommodation = AccommodationPreference(primary=accommodation)
            else:
                p.accommodation.primary = accommodation

    if "PROVIDE_ACCOMMODATION_PATTERN" in intents:
        pattern = extract_every_n_pattern(text)
        if pattern:
            primary, alt, n = pattern
            p.accommodation = AccommodationPreference(primary=primary, alt=alt, alt_every_n_nights=n)
    return p


def missing_fields(preference: TripPreferences) -> list[str]:
    missing = []
    if not preference.origin:
        missing.append("origin")
    if not preference.destination:
        missing.append("destination")
    if not preference.daily_distance_km:
        missing.append("daily distance")
    if not preference.start_month:
        missing.append("start month")
    if not preference.accommodation or not preference.accommodation.primary:
        missing.append("accommodation")
    return missing


def build_question(missing: list[str]):
    questions = []

    if "origin" in missing or "destination" in missing:
        questions.append("Where are you starting and where do you want to finish?")

    if "daily_distance_km" in missing:
        questions.append("Roughly how many km per day is comfortable for you?")

    if "month" in missing:
        questions.append("Which month are you travelling?")

    if "accommodation" in missing:
        questions.append("Do you prefer camping, hostels, or hotels? Any pattern (e.g., hostel every 4th night)?")

    return " ".join(questions[:2])
