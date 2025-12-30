from datetime import date, timedelta

def week_range(d: date) -> tuple[str, str]:
    # ISO week: måndag som start
    start = d - timedelta(days=d.weekday())
    end = start + timedelta(days=6)
    return start.isoformat(), end.isoformat()

def previous_week_range(d: date) -> tuple[str, str]:
    start, _ = week_range(d)
    start_d = date.fromisoformat(start) - timedelta(days=7)
    return week_range(start_d)
