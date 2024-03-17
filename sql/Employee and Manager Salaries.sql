#https://platform.stratascratch.com/coding/9894-employee-and-manager-salaries?code_type=1
SELECT
        a.first_name AS employee_name, 
        a.salary AS employee_salary
FROM employee AS a 
JOIN employee AS b ON  a.manager_id = b.id
WHERE a.salary > b.salary;
