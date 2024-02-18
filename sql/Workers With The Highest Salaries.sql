# https://platform.stratascratch.com/coding/10353-workers-with-the-highest-salaries?code_type=1
WITH subq as (
    select worker_id,
        salary,
        worker_title
    from worker
        inner join title on worker_id = worker_ref_id
)
SELECT distinct(worker_title)
from subq
where salary =(
        select max(salary)
        from subq
    )