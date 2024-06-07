/*https://platform.stratascratch.com/coding/2005-share-of-active-users?code_type=1*/
select count(
        case
            when status = 'open' then 1
            else null
        end
    )::decimal / count(*) as active_users_share
from fb_active_users
where country = 'USA'