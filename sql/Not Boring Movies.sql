/*https://leetcode.com/problems/not-boring-movies*/
select *
from Cinema
where id %2 != 0
    and instr(description, 'boring') = 0
order by rating desc