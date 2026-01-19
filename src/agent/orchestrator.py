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
from src.agent.planner import build_trip_plan
from src.agent.render import render_trip_plan
from src.agent.state import get_or_create_state, append_history
from src.demo_data import VECTORIZE, CORPUS_VECS, INTENT_LABELS
from src.schemas.api import ChatResponse
from src.schemas.tools import GetRouteRequest
from src.schemas.trip import TripPreferences, AccommodationPreference
from src.tools.route import get_route
from src.utils.intent_matching import classify_message

PREF_ORIGIN_STRING = "origin"
PREF_DESTINATION_STRING = "destination"
PREF_DAILY_DISTANCE_STRING = "daily distance"
PREF_START_MONTH_STRING = "start month"
PREF_ACCOMMODATION_PRIMARY_STRING = "accommodation"


def handle_message(session_id: str, message: str) -> ChatResponse:
    # get the state
    state = get_or_create_state(session_id)
    append_history(state, "user", message)

    # update the preferences
    old_preference = state.preferences
    new_preference = update_preferences_from_text(message, old_preference)

    is_preference_changed = preferences_changed(old_preference, new_preference)
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

    plan = state.last_plan
    if plan is None or is_preference_changed:
        plan = generate_plan(new_preference)
        try:
            state.last_plan = plan
        except Exception:
            pass

    reply = render_trip_plan(plan)
    append_history(state, "assistant", reply)
    return ChatResponse(
        session_id=session_id,
        reply=reply
    )


def preferences_changed(old_preference: TripPreferences, new_preference: TripPreferences):
    return old_preference.origin != new_preference.origin or \
        old_preference.destination != new_preference.destination or \
        old_preference.daily_distance_km != new_preference.daily_distance_km or \
        old_preference.start_month != new_preference.start_month or \
        old_preference.accommodation != new_preference.accommodation


def generate_plan(preference: TripPreferences):
    route = get_route(
        GetRouteRequest(origin=preference.origin, destination=preference.destination,
                        daily_distance_km=preference.daily_distance_km)
    )

    plan = build_trip_plan(
        preference, route
    )
    return plan


def update_preferences_from_text(text: str, old_preference: TripPreferences):
    intents = classify_message(
        text=text,
        vectorize=VECTORIZE,
        corpus_vecs=CORPUS_VECS,
        labels=INTENT_LABELS
    )
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
        missing.append(PREF_ORIGIN_STRING)
    if not preference.destination:
        missing.append(PREF_DESTINATION_STRING)
    if not preference.daily_distance_km:
        missing.append(PREF_DAILY_DISTANCE_STRING)
    if not preference.start_month:
        missing.append(PREF_START_MONTH_STRING)
    if not preference.accommodation or not preference.accommodation.primary:
        missing.append(PREF_ACCOMMODATION_PRIMARY_STRING)
    return missing


def build_question(missing: list[str]):
    questions = []

    if PREF_ORIGIN_STRING in missing or PREF_DESTINATION_STRING in missing:
        questions.append("Where are you starting and where do you want to finish?")

    if PREF_DAILY_DISTANCE_STRING in missing:
        questions.append("Roughly how many km per day is comfortable for you?")

    if PREF_START_MONTH_STRING in missing:
        questions.append("Which month are you travelling?")

    if PREF_ACCOMMODATION_PRIMARY_STRING in missing:
        questions.append("Do you prefer camping, hostels, or hotels? Any pattern (e.g., hostel every 4th night)?")

    return " ".join(questions[:2])
