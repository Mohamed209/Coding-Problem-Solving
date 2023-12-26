SELECT (
        SELECT count(user_id) as mobile_views
        FROM viewership
        where device_type in ('tablet', 'phone')
    ) as mobile_views,
    (
        SELECT count(user_id) as laptop_views
        FROM viewership
        where device_type = 'laptop'
    ) as laptop_views