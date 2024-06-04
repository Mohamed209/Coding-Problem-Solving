/*https://platform.stratascratch.com/coding/9650-find-the-top-10-ranked-songs-in-2010?code_type=1*/
select distinct year_rank as rank,
    group_name,
    song_name
from billboard_top_100_year_end
where year = 2010
    and year_rank between 1 and 10
order by year_rank