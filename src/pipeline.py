
from extract import extract
from transform import transform
from load import load

def run_pipeline() -> None:
    raw = extract()
    clean_jobs, job_skills = transform(raw)
    load(clean_jobs, job_skills)
    print(f"Loaded {len(clean_jobs)} job postings and {len(job_skills)} job-skill rows.")

if __name__ == "__main__":
    run_pipeline()
