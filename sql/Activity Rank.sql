# https://platform.stratascratch.com/coding/10351-activity-rank?code_type=1
with subq as (
    select from_user,
        count(from_user) as total_emails
    from google_gmail_emails
    group by from_user
    order by total_emails desc
)
select *,
    row_number() OVER(
        ORDER BY total_emails desc,
            from_user asc
    )
from subq