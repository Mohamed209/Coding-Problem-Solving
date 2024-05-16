/*https://platform.stratascratch.com/coding/10134-spam-posts?code_type=1*/
select post_date,
    (
        SUM(
            CASE
                when p.post_keywords LIKE '%spam%' then 1
                else 0
            end
        ) / CAST(COUNT(*) as float) * 100
    ) as spam_share
from facebook_posts p
    join facebook_post_views v on p.post_id = v.post_id
group by post_date