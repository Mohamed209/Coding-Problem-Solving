# https://platform.stratascratch.com/coding/10156-number-of-units-per-nationality?code_type=1
select nationality,
    count(distinct(unit_id)) as apartment_count
from airbnb_hosts
    inner join airbnb_units on airbnb_hosts.host_id = airbnb_units.host_id
where unit_type = 'Apartment'
    and age < 30
group by nationality