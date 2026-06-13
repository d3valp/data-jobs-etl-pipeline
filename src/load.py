
from pathlib import Path
import pandas as pd

OUT_DIR = Path(__file__).resolve().parents[1] / "data" / "processed"

def load(clean_jobs: pd.DataFrame, job_skills: pd.DataFrame) -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    clean_jobs.to_csv(OUT_DIR / "fact_job_postings.csv", index=False)
    job_skills.to_csv(OUT_DIR / "bridge_job_skills.csv", index=False)
