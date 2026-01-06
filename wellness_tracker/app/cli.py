from datetime import date
from tabulate import tabulate
from colorama import init, Fore, Style

from wellness_tracker.core.config import Settings, ensure_dirs
from wellness_tracker.core.logger import build_logger
from wellness_tracker.core.db import connect
from wellness_tracker.core.input import ask_choice, ask_int, ask_date

from wellness_tracker.yoga.service import build_session as build_yoga_session
from wellness_tracker.yoga import repo as yoga_repo

from wellness_tracker.meditation import repo as med_repo
from wellness_tracker.meditation.chakras import describe as chakra_describe
from wellness_tracker.meditation.service import (
    build_session as build_meditation_session,
    recommend_technique,
)

from wellness_tracker.reports.weekly import week_range, previous_week_range
from wellness_tracker.yoga.knowledge import describe_yoga, list_yoga_styles
from wellness_tracker.meditation.knowledge import describe_meditation, list_meditation_techniques


init(autoreset=True)


def run() -> None:
    settings = Settings()
    ensure_dirs(settings)
    logger = build_logger("wellness", str(settings.log_file))

    logger.info("✨App started✨")

    weight_kg = 55.0 

    while True:
        print("\n========================================")
        print("          WELLNESS TRACKER")
        print("========================================\n")
        print("1. Yoga")
        print("2. Meditation")
        print("3. Rapporter (vecka)")
        print("4. Kalender (denna vecka)")
        print("5. Chakra & meditation (info)")
        print("6. Kunskap: yoga & meditation")
        print("0. Avsluta")

        choice = ask_choice("Välj: ", {"0", "1", "2", "3", "4", "5", "6"})

        if choice == "0":
            logger.info("App exit")
            print("Hejdå!")
            return

        elif choice == "1":
            yoga_menu(settings, logger, weight_kg)

        elif choice == "2":
            meditation_menu(settings, logger)

        elif choice == "3":
            reports_menu(settings)

        elif choice == "4":
            calendar_menu(settings)

        elif choice == "5":
            chakra_menu()

        elif choice == "6":
            knowledge_menu()


def yoga_menu(settings: Settings, logger, weight_kg: float) -> None:
    with connect(settings.db) as con:
        print("\n--- YOGA ---")
        print("1. Lägg till yogapass")
        print("2. Visa senaste 3 pass")
        print("0. Tillbaka")

        c = ask_choice("Välj: ", {"0", "1", "2"})

        if c == "0":
            return

        elif c == "1":
            d = ask_date("Datum (YYYY-MM-DD): ")
            duration = ask_int("Minuter: ", 5, 300)
            style = input("Stil (Yin/Hatha/Flow/Vinyasa/Power): ").strip() or "Hatha"
            mood = ask_int("Humör (1-10): ", 1, 10)
            stress = ask_int("Stress (1-10): ", 1, 10)

            session = build_yoga_session(d, duration, style, mood, stress, weight_kg)
            yoga_repo.insert(con, session)

            logger.info(
                f"Yoga added {session.date} {session.duration}min {session.style} "
                f"mood={session.mood} stress={session.stress} calories={session.calories}"
            )
            print(Fore.GREEN + "Sparat! ✅" + Style.RESET_ALL)

        elif c == "2":
            rows = yoga_repo.list_recent(con, 3)
            if not rows:
                print("Inga yogapass än.")
                return

            table = [
                [r["date"], r["duration"], r["style"], r["mood"], r["stress"], r["calories"]]
                for r in rows
            ]
            print(tabulate(
                table,
                headers=["Datum", "Min", "Stil", "Humör", "Stress", "Kalorier"],
                tablefmt="grid"
            ))


def meditation_menu(settings: Settings, logger) -> None:
    with connect(settings.db) as con:
        print("\n--- MEDITATION ---")
        print("1. Lägg till meditation")
        print("2. Visa senaste 3 ")
        print("0. Tillbaka")

        c = ask_choice("Välj: ", {"0", "1", "2"})

        if c == "0":
            return

        elif c == "1":
            d = ask_date("Datum (YYYY-MM-DD): ")
            duration = ask_int("Minuter: ", 3, 180)
            technique = input("Teknik (andning/body scan/metta/mantra): ").strip() or "andning"
            chakra = input("Chakra (Root/Heart/... eller tom): ").strip() or None
            mood = ask_int("Humör (1-10): ", 1, 10)
            stress = ask_int("Stress (1-10): ", 1, 10)

            session = build_meditation_session(d, duration, technique, chakra, mood, stress)
            med_repo.insert(con, session)

            tip = recommend_technique(session.stress)
            print(Fore.CYAN + f"Tips (baserat på stress): {tip}" + Style.RESET_ALL)

            if session.chakra:
                print(
                    Fore.MAGENTA
                    + f"Chakra-fokus: {session.chakra} – {chakra_describe(session.chakra)}"
                    + Style.RESET_ALL
                )

            logger.info(
                f"Meditation added {session.date} {session.duration}min "
                f"{session.technique} chakra={session.chakra} mood={session.mood} stress={session.stress}"
            )
            print(Fore.GREEN + "Sparat! ✅" + Style.RESET_ALL)

        elif c == "2":
            rows = med_repo.list_recent(con, 3)
            if not rows:
                print("Inga meditationer än.")
                return

            table = [
                [r["date"], r["duration"], r["technique"], r["chakra"], r["mood"], r["stress"]]
                for r in rows
            ]
            print(tabulate(
                table,
                headers=["Datum", "Min", "Teknik", "Chakra", "Humör", "Stress"],
                tablefmt="grid"
            ))


def reports_menu(settings: Settings) -> None:
    today = date.today()
    w_start, w_end = week_range(today)
    p_start, p_end = previous_week_range(today)

    with connect(settings.db) as con:
        yoga_this = yoga_repo.total_minutes_week(con, w_start, w_end)
        med_this = med_repo.total_minutes_week(con, w_start, w_end)

        yoga_prev = yoga_repo.total_minutes_week(con, p_start, p_end)
        med_prev = med_repo.total_minutes_week(con, p_start, p_end)

    print("\n--- VECKORAPPORT ---")
    print(f"Denna vecka: {w_start} → {w_end}")
    print(f"Yoga: {yoga_this} min (skillnad: {yoga_this - yoga_prev} min)")
    print(f"Meditation: {med_this} min (skillnad: {med_this - med_prev} min)")


def calendar_menu(settings: Settings) -> None:
    today = date.today()
    w_start, w_end = week_range(today)

    with connect(settings.db) as con:
        yoga_rows = yoga_repo.list_week(con, w_start, w_end)

    print("\n--- KALENDER (YOGA DENNA VECKA) ---")
    if not yoga_rows:
        print("Inga yogapass denna vecka.")
        return

    table = [
        [r["date"], r["duration"], r["style"], r["calories"]]
        for r in yoga_rows
    ]
    print(tabulate(
        table,
        headers=["Datum", "Min", "Stil", "Kalorier"],
        tablefmt="grid"
    ))


def chakra_menu() -> None:
    print("\n--- CHAKRA & MEDITATION (GRUND) ---")
    name = input("Skriv chakra (Root / Sacral / Solar Plexus / Heart / Throat / Third Eye / Crown): ").strip().lower()
    print(chakra_describe(name))


def knowledge_menu() -> None:
    print("\n--- KUNSKAP: YOGA & MEDITATION ---")
    print("1. Yoga: välj stil")
    print("2. Meditation: välj teknik")
    print("0. Tillbaka")

    choice = ask_choice("Välj: ", {"0", "1", "2"})

    if choice == "0":
        return

    if choice == "1":
        styles = list_yoga_styles()
        print("\nTillgängliga yogastilar:")
        for i, s in enumerate(styles, start=1):
            print(f"{i}. {s}")

        idx = ask_int("Välj nummer: ", 1, len(styles))
        selected = styles[idx - 1]
        print("\n" + describe_yoga(selected))

    elif choice == "2":
        techniques = list_meditation_techniques()
        print("\nTillgängliga meditationstekniker:")
        for i, t in enumerate(techniques, start=1):
            print(f"{i}. {t}")

        idx = ask_int("Välj nummer: ", 1, len(techniques))
        selected = techniques[idx - 1]
        print("\n" + describe_meditation(selected))

