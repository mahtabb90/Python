from __future__ import annotations

from .models import MeditationSession
from .chakras import CHAKRAS


TECHNIQUE_ALIASES = {
    "andning": "Andning",
    "breath": "Andning",
    "body scan": "Body scan",
    "bodyscan": "Body scan",
    "metta": "Metta",
    "loving kindness": "Metta",
    "mantra": "Mantra",
}


def normalize_technique(raw: str) -> str:
    """Gör tekniken konsekvent (samma stavning i databasen)."""
    key = raw.strip().lower()
    return TECHNIQUE_ALIASES.get(key, raw.strip().title() or "Andning")


def normalize_chakra(raw: str) -> str | None:
    """Returnerar None om tomt, annars en 'känd' chakra eller originaltext."""
    value = raw.strip()
    if not value:
        return None

    # försök matcha kända chakran case-insensitive
    for name in CHAKRAS.keys():
        if value.lower() == name.lower():
            return name

    return value  # om användaren skrev något annat


def validate_scale(name: str, value: int, min_value: int = 1, max_value: int = 10) -> int:
    if value < min_value or value > max_value:
        raise ValueError(f"{name} måste vara mellan {min_value} och {max_value}.")
    return value


def validate_duration(duration: int) -> int:
    if duration < 3 or duration > 180:
        raise ValueError("Minuter för meditation måste vara mellan 3 och 180.")
    return duration


def build_session(
    date: str,
    duration: int,
    technique: str,
    chakra: str | None,
    mood: int,
    stress: int,
) -> MeditationSession:
    """Bygger ett MeditationSession-objekt med validering och normalisering."""
    duration = validate_duration(duration)
    mood = validate_scale("Humör", mood)
    stress = validate_scale("Stress", stress)

    technique_norm = normalize_technique(technique)
    chakra_norm = normalize_chakra(chakra or "")

    return MeditationSession(
        date=date,
        duration=duration,
        technique=technique_norm,
        chakra=chakra_norm,
        mood=mood,
        stress=stress,
    )


def recommend_technique(stress: int) -> str:
    """En enkel rekommendation baserat på stressnivå (extra funktion)."""
    if stress >= 8:
        return "Andning (4-6 andning) eller Body scan"
    if stress >= 5:
        return "Andning eller Metta"
    return "Mantra eller tyst meditation"
