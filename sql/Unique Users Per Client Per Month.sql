/*https://platform.stratascratch.com/coding/2024-unique-users-per-client-per-month?code_type=1*/
select client_id,
    date_part('month', time_id) as month,
    count(distinct(user_id)) as users_num
from fact_events
group by client_id,
    month