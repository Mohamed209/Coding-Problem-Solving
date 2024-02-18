# https://platform.stratascratch.com/coding/10064-highest-energy-consumption
with subq2 AS (
    select date,
        sum(consumption) as total
    from (
            select *
            from fb_eu_energy
            union all
            select *
            from fb_asia_energy
            union all
            select *
            from fb_na_energy
        ) as subq1
    group by date
    order by date
)
select *
from subq2
WHERE total =(
        SELECT max(total)
        from subq2
    )