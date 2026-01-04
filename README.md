🧘‍♀️ Wellness Tracker – CLI-program i Python
 beskrivning:

Wellness Tracker är ett terminalbaserat (CLI) Python-program som används för att registrera, analysera och följa upp yoga- och meditationspass.

Programmet är byggt med en modulär och projektstruktur, använder MySQL som databas och är utvecklat med fokus på:

. tydlig kodstruktur

. säker hantering av användarinput

. loggning

. analys och rapportering


🧱Projektstruktur:


wellness_tracker/
├── main.py
├── pyproject.toml
├── README.md
├── requirements.txt
└── wellness_tracker/
    ├── __init__.py
    ├── app/
    │   ├── __init__.py
    │   └── cli.py
    ├── core/
    │   ├── __init__.py
    │   ├── config.py
    │   ├── logger.py
    │   ├── db.py
    │   └── input.py
    ├── yoga/
    │   ├── __init__.py
    │   ├── models.py
    │   ├── repo.py
    │   ├── service.py
    │   └── knowledge.py
    ├── meditation/
    │   ├── __init__.py
    │   ├── models.py
    │   ├── repo.py
    │   ├── service.py
    │   ├── knowledge.py
    │   └── chakras.py
    └── reports/
        ├── __init__.py
        └── weekly.py





🎯 Vad gör programmet?

Programmet låter användaren:

🧘 registrera yogapass (tid, stil, humör, stress, kalorier)

🧘‍♂️ registrera meditationspass (teknik, chakra, humör, stress)

📊 se veckorapporter och jämföra med föregående vecka

📅 visa kalenderöversikt för aktuell vecka

🧠 läsa kunskapstexter om yoga, meditation och chakran

🔐 använda säker validering av användarinput

🗄️ spara all data i en MySQL-databas

All data sparas permanent i databasen och finns kvar mellan körningar.


 🧱Projektstruktur (förklaringar):


📄 Root-filer

main.py
Startpunkt för programmet. Importerar och kör CLI:t.

pyproject.toml
Projektets metadata, beroenden och CLI-kommando (wellness-tracker).

requirements.txt
Lista över externa beroenden (t.ex. colorama, tabulate, mysql-connector-python).

README.md
Dokumentation av projektet .

📦 Paket: wellness_tracker/
app/

cli.py
Huvudmeny och all användarinteraktion i terminalen.
Anropar service- och repo-lager beroende på användarens val.

core/

Kärnfunktioner som används av hela projektet.

config.py
Samlar konfiguration (loggfil, MySQL-inställningar).
Gör det enkelt att ändra miljö utan att röra affärslogik.

db.py
Hanterar MySQL-anslutning via context manager (with connect(...)).

logger.py
Custom logger med olika loggnivåer (INFO, ERROR m.m.).

input.py
Säker hantering och validering av användarinput.

yoga/

All logik som rör yogapass.

models.py
Klass som representerar ett yogapass (dataobjekt).

repo.py
Databasoperationer (INSERT, SELECT) för yoga.

service.py
Affärslogik, t.ex. kaloriberäkning och skapande av yogasession.

knowledge.py
Kunskapstexter om olika yogastilar.

meditation/

All logik som rör meditation.

models.py
Klass för meditationssessioner.

repo.py
Databasoperationer för meditation.

service.py
Affärslogik, t.ex. rekommendationer baserat på stressnivå.

knowledge.py
Beskrivningar av meditationstekniker.

chakras.py
Grundläggande information om chakran och hur meditation påverkar dem.

reports/

weekly.py
Funktioner för veckoberäkningar och jämförelse mellan veckor.

-Jag använder __init__.py för att definiera tydliga Python-paket och dokumentera syftet med varje del av projektet.
Det gör strukturen lättare att förstå och underhålla.

🗄️ Databas

Projektet använder MySQL som extern relationsdatabas.

Separat databas: wellness

Separat användare: wellness_user (inte root)

Två huvudtabeller:

   .yoga_sessions

   .meditation_sessions

Detta gör projektet mer realistiskt och säkrare.

▶️ Hur man installerar projektet

Skapa och aktivera virtuell miljö

python -m venv .venv
source .venv/Scripts/activate


Installera beroenden

pip install -r requirements.txt


Installera projektet lokalt

pip install -e .

▶️ Hur man kör programmet
winpty wellness-tracker