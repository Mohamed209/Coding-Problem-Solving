#https://platform.stratascratch.com/coding/10544-high-density-areas?code_type=1
select area_name,
    count(distinct(customer_id)) / avg(area_size) as denisty
from transaction_records
    inner join stores using(store_id)
group by area_name
order by denisty desc