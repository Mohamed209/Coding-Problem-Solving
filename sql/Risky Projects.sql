# https://platform.stratascratch.com/coding/10304-risky-projects?code_type=1
with subq as (
    select *,
        (end_date - start_date) / 365.0 as proj_duration_days
    from linkedin_projects
        inner join linkedin_emp_projects on linkedin_projects.id = linkedin_emp_projects.project_id
        inner join linkedin_employees on linkedin_emp_projects.emp_id = linkedin_employees.id
)
select title,
    budget,
    ceiling(sum(salary) * max(proj_duration_days)) as cost
from subq
group by title,
    budget
having sum(salary) * max(proj_duration_days) > budget
order by title asc