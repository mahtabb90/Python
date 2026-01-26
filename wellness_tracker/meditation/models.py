from dataclasses import dataclass

@dataclass
class MeditationSession:
    date: str
    duration: int
    technique: str
    chakra: str | None = None
    mood: int | None = None
    stress: int | None = None
