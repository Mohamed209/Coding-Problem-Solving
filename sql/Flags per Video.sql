/*https://platform.stratascratch.com/coding/2102-flags-per-video?code_type=1*/
select video_id,
    count(distinct(concat(user_firstname, user_lastname)))
from user_flags
where flag_id is not null
group by video_id