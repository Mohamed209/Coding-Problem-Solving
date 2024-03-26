#https://platform.stratascratch.com/coding/9897-highest-salary-in-department?code_type=1 
with q1 as
    (select department,
            max(salary)
     from employee
     group by department)
select q1.department,
       employee.first_name as employee_name,
       q1.max as salary
from q1
inner join employee on q1.department=employee.department
and q1.max=employee.salary