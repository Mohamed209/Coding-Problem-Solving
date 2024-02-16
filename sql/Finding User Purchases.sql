# https://platform.stratascratch.com/coding/10322-finding-user-purchases/
with subq as (
    select user_id,
        created_at - lag(created_at) over (
            Partition by user_id
            order by created_at
        ) as time_from_last_purchase
    from amazon_transactions
)
select distinct(user_id)
from subq
where time_from_last_purchase <= 7