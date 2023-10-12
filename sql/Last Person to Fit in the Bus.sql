# https://leetcode.com/problems/last-person-to-fit-in-the-bus/description/
select person_name
from (
        select person_name,
            turn,
            sum(weight) over (
                order by turn
            ) as moving_sum
        from Queue
    ) as derived_table
where moving_sum <= 1000
order by turn desc
limit 1