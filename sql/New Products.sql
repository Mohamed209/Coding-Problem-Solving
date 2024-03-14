# https://platform.stratascratch.com/coding/10318-new-products?code_type=1
with year_2019(company_name, no_cars) as (
    select company_name,
        count(product_name) as no_cars
    from car_launches
    where year = 2019
    group by company_name
),
year_2020(company_name, no_cars) as (
    select company_name,
        count(product_name) as no_cars
    from car_launches
    where year = 2020
    group by company_name
)
select a.company_name,
    b.no_cars - a.no_cars as net_difference
from year_2019 a
    join year_2020 b on a.company_name = b.company_name