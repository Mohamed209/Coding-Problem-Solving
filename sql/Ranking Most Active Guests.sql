#https://platform.stratascratch.com/coding/10159-ranking-most-active-guests?code_type=1
with aggsubq as (
    select id_guest,
        sum(n_messages) as sum_n_messages
    from airbnb_contacts
    group by id_guest
)
select dense_rank() over (
        order by sum_n_messages desc
    ) as ranking,
    id_guest,
    sum_n_messages
from aggsubq