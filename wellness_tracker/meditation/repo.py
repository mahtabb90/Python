
from .models import MeditationSession

def insert(con, s) -> None:
    cur = con.cursor()
    cur.execute(
        "INSERT INTO meditation_sessions(date, duration, technique, chakra, mood, stress) VALUES(%s,%s,%s,%s,%s,%s)",
        (s.date, s.duration, s.technique, s.chakra, s.mood, s.stress),
    )
    con.commit()
    cur.close()

def list_recent(con, n: int = 3):
    cur = con.cursor(dictionary=True)
    cur.execute("SELECT * FROM meditation_sessions ORDER BY date DESC, id DESC LIMIT %s", (n,))
    rows = cur.fetchall()
    cur.close()
    return rows

def total_minutes_week(con, week_start: str, week_end: str) -> int:
    cur = con.cursor(dictionary=True)
    cur.execute(
        "SELECT COALESCE(SUM(duration),0) AS total FROM meditation_sessions WHERE date >= %s AND date <= %s",
        (week_start, week_end),
    )
    total = int(cur.fetchone()["total"])
    cur.close()
    return total

