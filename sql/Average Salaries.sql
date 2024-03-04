with avgsal as (
    select department,
        avg(salary)
    from employee
    group by department
)
select avgsal.department,
    first_name,
    salary,
    avgsal.avg
from avgsal
    inner join employee on avgsal.department = employee.department