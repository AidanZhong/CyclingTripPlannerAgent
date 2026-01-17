# -*- coding: utf-8 -*-
"""
Created on 17/01/2026 22:01

@author: Aidan
@project: CyclingTripPlannerAgent
@filename: extractor
"""
import re
from typing import Optional, Tuple

MONTH_MAP = {
    "january": "January", "jan": "January",
    "february": "February", "feb": "February",
    "march": "March", "mar": "March",
    "april": "April", "apr": "April",
    "may": "May",
    "june": "June", "jun": "June",
    "july": "July", "jul": "July",
    "august": "August", "aug": "August",
    "september": "September", "sep": "September", "sept": "September",
    "october": "October", "oct": "October",
    "november": "November", "nov": "November",
    "december": "December", "dec": "December",
}

NON_LOCATION_WORDS = {
    "km", "kilometer", "kilometre", "mile", "miles",
    "day", "days", "daily", "night", "nights",
    "january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november",
    "december",
    "camping", "camp", "hostel", "hostels", "hotel", "hotels",
}


def _clean_location(s: str) -> str:
    s = s.strip().strip('"\'')
    s = re.sub(r"[.,;:!?]+$", "", s).strip()
    s = re.sub(r"\s+", " ", s).strip()
    return s


def _looks_like_location(s: str) -> bool:
    if not s:
        return False
    low = s.lower().strip()
    if len(low) < 2:
        return False
    # reject if contains obvious non-location terms
    tokens = re.findall(r"[a-z]+", low)
    if any(t in NON_LOCATION_WORDS for t in tokens):
        return False
    # should contain letters
    if not re.search(r"[A-Za-z]", s):
        return False
    return True


# Route extraction

def extract_route(text: str) -> Tuple[Optional[str], Optional[str]]:
    t = text.strip()
    # from X to Y
    m = re.search(r"\bfrom\s+(.+?)\s+to\s+(.+?)(?:[.,;]|$)", t, re.I)
    if m:
        origin = _clean_location(m.group(1))
        dest = _clean_location(m.group(2))
        if _looks_like_location(origin) and _looks_like_location(dest) and origin.lower() != dest.lower():
            return origin, dest

    # X -> Y or X → Y
    m = re.search(r"(.+?)\s*(?:->|→)\s*(.+?)(?:[.,;]|$)", t)
    if m:
        origin = _clean_location(m.group(1))
        dest = _clean_location(m.group(2))
        if _looks_like_location(origin) and _looks_like_location(dest) and origin.lower() != dest.lower():
            return origin, dest

    return None, None


# Daily distance extraction

def extract_daily_distance(text: str) -> Optional[int]:
    low = text.lower()

    # Pattern like "100-120km/day" or "100 km/day"
    m = re.search(r"(\d{2,3})(?:\s*-\s*\d{2,3})?\s*km\s*(?:a\s*day|per\s*day|/day|daily)\b", low)
    if m:
        km = int(m.group(1))
        if 10 <= km <= 300:
            return km

    # Reverse wording: "per day ... 100 km"
    m = re.search(r"(?:a\s*day|per\s*day|/day|daily).{0,20}?(\d{2,3})\s*km\b", low)
    if m:
        km = int(m.group(1))
        if 10 <= km <= 300:
            return km

    return None


# Month extraction

def extract_month(text: str) -> Optional[str]:
    low = text.lower()
    # scan by word boundary to avoid matching inside other words
    for k, v in MONTH_MAP.items():
        if re.search(rf"\b{k}\b", low):
            return v
    return None


# Primary accommodation extraction

def extract_primary_accommodation(text: str) -> Optional[str]:
    low = text.lower()

    if re.search(r"\bcamp(ing)?\b", low) or "campsite" in low or "camp site" in low:
        return "camping"
    if re.search(r"\bhostel(s)?\b", low):
        return "hostel"
    if re.search(r"\bhotel(s)?\b", low):
        return "hotel"
    return None


# Every-N pattern extraction

def extract_every_n_pattern(text: str, primary_hint: Optional[str] = None, ) -> Optional[Tuple[str, str, int]]:
    low = text.lower()

    # extract N
    m = re.search(r"every\s+(\d+)(?:st|nd|rd|th)?\s+night\b", low)
    if not m:
        m = re.search(r"every\s+(\d+)\s+nights?\b", low)
    if not m:
        return None

    n = int(m.group(1))
    if n < 2 or n > 30:
        return None

    # detect mentioned accommodation
    has_camping = bool(re.search(r"\bcamp(ing)?\b", low) or "campsite" in low or "camp site" in low)
    has_hostel = bool(re.search(r"\bhostel(s)?\b", low))
    has_hotel = bool(re.search(r"\bhotel(s)?\b", low))

    mentioned = []
    if has_camping: mentioned.append("camping")
    if has_hostel: mentioned.append("hostel")
    if has_hotel: mentioned.append("hotel")

    # alt: prefer hostel/hotel if present
    alt = None
    if has_hostel:
        alt = "hostel"
    elif has_hotel:
        alt = "hotel"
    elif has_camping:
        alt = "camping"

    if not alt:
        return None

    # determine primary
    primary = None
    # If two more types mentioned, pick the other one as primary
    if len(mentioned) >= 2:
        if alt != "camping" and has_camping:
            primary = "camping"
        elif alt != "hostel" and has_hostel:
            primary = "hostel"
        elif alt != "hotel" and has_hotel:
            primary = "hotel"
    else:
        if primary_hint and primary_hint in {"camping", "hostel", "hotel"} and primary_hint != alt:
            primary = primary_hint

    if not primary or primary == alt:
        return None

    return (primary, alt, n)
