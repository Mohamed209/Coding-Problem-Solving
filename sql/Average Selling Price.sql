# Write your MySQL query statement below
# https://leetcode.com/problems/average-selling-price/description/
SELECT p.product_id,
    IFNULL(ROUND(SUM(units * price) / SUM(units), 2), 0) AS average_price
FROM Prices as p
    LEFT JOIN UnitsSold as u ON p.product_id = u.product_id
    AND u.purchase_date BETWEEN start_date AND end_date
group by product_id