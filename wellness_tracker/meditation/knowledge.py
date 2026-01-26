MEDITATION_TYPES = {
    "Andning": {
        "description": "Fokus på andetaget.",
        "benefit": "Minskar stress och lugnar nervsystemet.",
        "how": "Observera in- och utandning utan att ändra."
    },
    "Body scan": {
        "description": "Medveten närvaro i kroppen.",
        "benefit": "Ökar kroppsmedvetenhet.",
        "how": "Flytta uppmärksamheten långsamt genom kroppen."
    },
    "Metta": {
        "description": "Kärleksfull vänlighet.",
        "benefit": "Ökar empati och lugn.",
        "how": "Upprepa vänliga fraser mentalt."
    },
    "Mantra": {
        "description": "Upprepning av ljud eller ord.",
        "benefit": "Förbättrar fokus.",
        "how": "Upprepa mantrat i takt med andetaget."
    },
}

def describe_meditation(name: str) -> str:
    info = MEDITATION_TYPES.get(name)
    if not info:
        return "Okänd meditationstyp."
    return (
        f"{name}\n"
        f"Beskrivning: {info['description']}\n"
        f"Effekt: {info['benefit']}\n"
        f"Hur: {info['how']}"
    )

def list_meditation_techniques() -> list[str]:
    """Returnerar alla tillgängliga meditationstekniker."""
    return sorted(MEDITATION_TYPES.keys())
