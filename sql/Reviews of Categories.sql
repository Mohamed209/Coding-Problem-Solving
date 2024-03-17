WITH cat AS
  (SELECT unnest(string_to_array(categories, ';')) AS category,
          review_count
   FROM yelp_business)
SELECT category,
       sum(review_count) AS review_cnt
FROM cat
GROUP BY category
ORDER BY review_cnt DESC
