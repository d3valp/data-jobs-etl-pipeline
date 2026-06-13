
SELECT
    j.title,
    s.skill,
    COUNT(*) AS skill_mentions,
    ROUND(AVG(j.salary_mid_eur), 0) AS avg_salary_mid_eur
FROM {{ ref('fact_job_postings') }} j
JOIN {{ ref('bridge_job_skills') }} s USING (job_id)
GROUP BY j.title, s.skill
