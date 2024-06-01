/*https://platform.stratascratch.com/coding/9781-find-the-rate-of-processed-tickets-for-each-type?code_type=1*/
select type,
       cast(sum(case
                    when processed=true then 1
                    else 0
                end)as float) /count(processed) processed_rate
from facebook_complaints
group by type