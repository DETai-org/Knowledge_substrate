import os
from dataclasses import dataclass
from pathlib import Path

from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parents[3]
load_dotenv(dotenv_path=BASE_DIR / '.env')


@dataclass(frozen=True)
class Settings:
    database_url: str
    api_title: str = 'DETai Core API'
    api_version: str = '0.2.0'



def get_settings() -> Settings:
    database_url = os.getenv('DATABASE_URL')
    if not database_url:
        raise RuntimeError('DATABASE_URL not found')
    return Settings(database_url=database_url)
