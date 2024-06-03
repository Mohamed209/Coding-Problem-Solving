/*https://platform.stratascratch.com/coding/9728-inspections-that-resulted-in-violations?code_type=1*/
select date_part('year', inspection_date) as year,
    count(violation_id) as n_inspections
from sf_restaurant_health_violations
where business_name = 'Roxanne Cafe'
group by year
order by year