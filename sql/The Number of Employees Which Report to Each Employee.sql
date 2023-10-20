/*https://leetcode.com/problems/the-number-of-employees-which-report-to-each-employee/*/
select Employees.employee_id,
    Employees.name,
    subquery.reports_count,
    subquery.average_age
from Employees
    inner join (
        select reports_to,
            count(employee_id) as reports_count,
            round(avg(age)) as average_age
        from Employees
        where reports_to is not null
        group by reports_to
    ) as subquery on employee_id = subquery.reports_to
order by employee_id