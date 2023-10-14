/*https://leetcode.com/problems/queries-quality-and-percentage/description/*/
select query_name,
    round(avg(rating / position), 2) as quality,
    round(
        sum(
            case
                when rating < 3 then 1
                else 0
            end
        ) / count(rating) * 100,
        2
    ) as poor_query_percentage
from Queries
group by query_name