from datetime import datetime

def ask_choice(prompt: str, valid: set[str]) -> str:
    while True:
        val = input(prompt).strip()
        if val in valid:
            return val
        print("Ogiltigt val. Försök igen.")

def ask_int(prompt: str, min_value: int | None = None, max_value: int | None = None) -> int:
    while True:
        raw = input(prompt).strip()
        try:
            num = int(raw)
        except ValueError:
            print("Skriv ett heltal.")
            continue
        if min_value is not None and num < min_value:
            print(f"Måste vara minst {min_value}.")
            continue
        if max_value is not None and num > max_value:
            print(f"Får vara max {max_value}.")
            continue
        return num

def ask_date(prompt: str) -> str:
    while True:
        raw = input(prompt).strip()
        try:
            datetime.strptime(raw, "%Y-%m-%d")
            return raw
        except ValueError:
            print("Fel format. Använd YYYY-MM-DD, t.ex. 2026-01-15.")
