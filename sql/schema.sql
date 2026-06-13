
CREATE TABLE fact_job_postings (
    job_id TEXT PRIMARY KEY,
    title TEXT,
    company TEXT,
    city TEXT,
    contract_type TEXT,
    seniority TEXT,
    salary_min_eur INTEGER,
    salary_max_eur INTEGER,
    salary_mid_eur INTEGER,
    remote_policy TEXT,
    skills TEXT,
    posted_date DATE,
    title_normalized TEXT
);

CREATE TABLE bridge_job_skills (
    job_id TEXT REFERENCES fact_job_postings(job_id),
    skill TEXT,
    PRIMARY KEY (job_id, skill)
);
