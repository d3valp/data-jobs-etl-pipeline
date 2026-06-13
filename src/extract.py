
from pathlib import Path
import pandas as pd

RAW_FILE = Path(__file__).resolve().parents[1] / "data" / "raw" / "job_postings_2026_sample.csv"

def extract() -> pd.DataFrame:
    """Extract raw job postings from CSV.

    This module is intentionally simple so it can later be replaced with an API or scraper.
    """
    if not RAW_FILE.exists():
        raise FileNotFoundError(f"Missing raw file: {RAW_FILE}")
    return pd.read_csv(RAW_FILE)
