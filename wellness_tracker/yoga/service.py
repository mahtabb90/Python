from .models import YogaSession

# Enkla MET-värden
MET_BY_STYLE = {
    "Yin": 2.0,
    "Hatha": 2.5,
    "Flow": 3.0,
    "Vinyasa": 3.0,
    "Power": 4.0,
}

def estimate_calories(duration_min: int, style: str, weight_kg: float = 70.0) -> float:
    met = MET_BY_STYLE.get(style, 2.5)
    # Standardformel: kcal/min = MET * 3.5 * kg / 200
    kcal = (met * 3.5 * weight_kg / 200.0) * duration_min
    return round(kcal, 1)

def build_session(date: str, duration: int, style: str, mood: int, stress: int, weight_kg: float) -> YogaSession:
    calories = estimate_calories(duration, style, weight_kg)
    return YogaSession(date=date, duration=duration, style=style, mood=mood, stress=stress, calories=calories)
