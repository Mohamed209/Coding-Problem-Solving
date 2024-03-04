with idloc as (
    select id as employee_id,
        location
    from facebook_employees
)
select location,
    avg(popularity)
from facebook_hack_survey
    inner join idloc using (employee_id)
group by location