/*https://platform.stratascratch.com/coding/9905-highest-target-under-manager?code_type=1*/
select first_name,
    target
from salesforce_employees
where manager_id = 13
    and target =(
        select max(target)
        from salesforce_employees
        where manager_id = 13
    )