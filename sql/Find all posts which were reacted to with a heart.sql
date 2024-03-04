with heart as (
    select distinct(post_id)
    from facebook_reactions
    where reaction = 'heart'
)
select *
from facebook_posts
    inner join heart using (post_id)