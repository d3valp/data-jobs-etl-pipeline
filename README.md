
# Data Jobs ETL Pipeline

A data engineering portfolio project that builds an end-to-end ETL pipeline for French data job postings.

## Project goal
Convert raw job-posting data into clean analytical tables that can support dashboards, SQL analysis, and machine learning projects.

## Architecture
```text
Raw CSV → Python extraction → schema validation → transformation → analytical CSV tables → SQL/dbt-ready models
```

## What this demonstrates
- Modular ETL design
- Data validation
- Normalization of many-to-many skill data
- SQL schema design
- dbt-style transformation thinking
- Clear documentation

## How to run
```bash
pip install -r requirements.txt
python src/pipeline.py
```

Outputs are written to:
```text
data/processed/fact_job_postings.csv
data/processed/bridge_job_skills.csv
```

## Dataset note
The included dataset is synthetic but realistic. It is intended for portfolio demonstration and can be replaced with collected data.

## Next improvements
- PostgreSQL loading
- Docker Compose setup
- Airflow orchestration
- Data quality test suite
- Streamlit monitoring dashboard
