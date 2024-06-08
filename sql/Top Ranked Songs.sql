/*https://platform.stratascratch.com/coding/9991-top-ranked-songs?code_type=1*/
select trackname,
    count(*) as times_top1
from spotify_worldwide_daily_song_ranking
where position = 1
group by trackname
order by times_top1 desc