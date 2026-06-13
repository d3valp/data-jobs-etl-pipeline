
import pandas as pd

REQUIRED_COLUMNS = {
    "job_id", "title", "company", "city", "contract_type", "seniority",
    "salary_min_eur", "salary_max_eur", "remote_policy", "skills", "posted_date"
}

def validate_schema(df: pd.DataFrame) -> None:
    missing = REQUIRED_COLUMNS - set(df.columns)
    if missing:
        raise ValueError(f"Missing columns: {sorted(missing)}")

def transform(df: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    validate_schema(df)
    clean = df.copy()
    clean["posted_date"] = pd.to_datetime(clean["posted_date"]).dt.date
    clean["salary_mid_eur"] = ((clean["salary_min_eur"] + clean["salary_max_eur"]) / 2).round(0).astype(int)
    clean["title_normalized"] = clean["title"].str.lower().str.replace(" ", "_", regex=False)
    clean = clean.drop_duplicates(subset=["job_id"])

    skills = (
        clean[["job_id", "skills"]]
        .assign(skill=lambda x: x["skills"].str.split(", "))
        .explode("skill")
        .drop(columns=["skills"])
        .drop_duplicates()
    )
    return clean, skills
