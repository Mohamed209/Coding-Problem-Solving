/*https://leetcode.com/problems/project-employees-i/description*/
select proj.project_id,
    round(avg(emp.experience_years), 2) as average_years
from Project as proj
    inner join Employee as emp on proj.employee_id = emp.employee_id
group by proj.project_id