from dataclasses import dataclass
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
LOG_DIR = PROJECT_ROOT / "logs"
LOG_FILE = LOG_DIR / "app.log"


@dataclass(frozen=True)
class DBConfig:
    host: str = "localhost"
    user: str = "wellness_user"
    password: str = "StrongPass123!"      
    database: str = "wellness"
    port: int = 3306


@dataclass(frozen=True)
class Settings:
    log_file: Path = LOG_FILE
    db: DBConfig = DBConfig()  


def ensure_dirs(settings: Settings) -> None:
    LOG_DIR.mkdir(exist_ok=True)
