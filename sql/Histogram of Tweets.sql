-- https://datalemur.com/questions/sql-histogram-tweets
SELECT tweet_bucket,
    COUNT(user_id) as users_num
from (
        SELECT user_id,
            COUNT(tweet_id) as tweet_bucket
        FROM tweets
        WHERE tweet_date BETWEEN '2022-01-01' AND '2022-12-31'
        GROUP BY user_id
    ) as subq
GROUP BY tweet_bucket