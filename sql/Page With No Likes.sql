-- https://datalemur.com/questions/sql-page-with-no-likes
SELECT pages.page_id
FROM pages
    left join page_likes on pages.page_id = page_likes.page_id
where user_id is NULL -- with no users like the page
ORDER BY pages.page_id