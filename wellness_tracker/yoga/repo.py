
from .models import YogaSession

def insert(con, s) -> None:
    cur = con.cursor()
    cur.execute(
        "INSERT INTO yoga_sessions(date, duration, style, mood, stress, calories) VALUES(%s,%s,%s,%s,%s,%s)",
        (s.date, s.duration, s.style, s.mood, s.stress, s.calories),
    )
    con.commit()
    cur.close()

def list_recent(con, n: int = 3):
    cur = con.cursor(dictionary=True)
    cur.execute("SELECT * FROM yoga_sessions ORDER BY date DESC, id DESC LIMIT %s", (n,))
    rows = cur.fetchall()
    cur.close()
    return rows

def list_week(con, week_start: str, week_end: str):
    cur = con.cursor(dictionary=True)
    cur.execute(
        "SELECT * FROM yoga_sessions WHERE date >= %s AND date <= %s ORDER BY date ASC",
        (week_start, week_end),
    )
    rows = cur.fetchall()
    cur.close()
    return rows

def total_minutes_week(con, week_start: str, week_end: str) -> int:
    cur = con.cursor(dictionary=True)
    cur.execute(
        "SELECT COALESCE(SUM(duration),0) AS total FROM yoga_sessions WHERE date >= %s AND date <= %s",
        (week_start, week_end),
    )
    total = int(cur.fetchone()["total"])
    cur.close()
    return total

