from dataclasses import dataclass

@dataclass
class YogaSession:
    date: str
    duration: int
    style: str
    mood: int | None = None      # 1-10
    stress: int | None = None    # 1-10
    calories: float | None = None

    def is_long(self) -> bool:
        return self.duration >= 45
