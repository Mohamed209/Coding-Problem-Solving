problem : https://www.hackerrank.com/challenges/earnings-of-employees/problem
query : select salary*months as "maximum total earnings" ,count(1) from Employee group by 1 order by 1 desc limit 1;
===============================================================================
problem : https://www.hackerrank.com/challenges/weather-observation-station-18/problem
query : select round(abs(min(LAT_N)-max(LAT_N))+abs(min(LONG_W)-max(LONG_W)),4) from STATION
===============================================================================
PROBLEM : https://www.hackerrank.com/challenges/weather-observation-station-19/problem
query : select round(sqrt((max(LAT_N)-min(LAT_N))*(max(LAT_N)-min(LAT_N))+(max(LONG_W)-min(LONG_W))*(max(LONG_W)-min(LONG_W))),4) from STATION
===============================================================================
problem : https://www.hackerrank.com/challenges/asian-population/problem
query : select sum(city.population) from city inner join country ON COUNTRY.CODE = CITY.COUNTRYCODE where country.CONTINENT='Asia'
===============================================================================
problem : https://www.hackerrank.com/challenges/average-population-of-each-continent/problem
query : select country.continent,floor(avg(city.population)) from city inner join country ON country.code = city.countrycode group by country.continent
===============================================================================
problem : https://www.hackerrank.com/challenges/full-score/problem
query : 
select h.hacker_id,h.name from hackers h,challenges c ,difficulty d,submissions s 
where h.hacker_id=s.hacker_id
and c.challenge_id=s.challenge_id
and c.difficulty_level=d.difficulty_level
and s.score=d.score
group by h.hacker_id,h.name having  count(h.hacker_id)>1
 order by count(c.challenge_id) desc,h.hacker_id;
 ============================================================================
