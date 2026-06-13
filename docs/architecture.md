
# Pipeline Architecture

```text
CSV source → extract.py → transform.py → load.py → processed CSV tables → SQL/dbt models
```

## Design choices
- Raw data is kept immutable in `data/raw`.
- Transformations create analytic tables in `data/processed`.
- Skills are normalized into a bridge table to support many-to-many analysis.
- The code is modular so CSV extraction can later be replaced by an API or scraper.

## Production improvements
- Add orchestration with Airflow or Prefect.
- Load to PostgreSQL instead of local CSV.
- Add data quality checks with Great Expectations or Pandera.
- Add CI tests for schema validation.
