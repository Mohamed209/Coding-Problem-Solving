# https://platform.stratascratch.com/coding/9915-highest-cost-orders?code_type=1
# Answer:
WITH daily_total_orders as (
    select cust_id,
        order_date,
        sum(total_order_cost) as total_order_cost
    from orders
    where order_date between '2019-02-01' and '2019-05-01'
    group by cust_id,
        order_date
    order by order_date
)
SELECT first_name,
    order_date,
    total_order_cost
from daily_total_orders
    INNER JOIN customers on daily_total_orders.cust_id = customers.id
where total_order_cost =(
        SELECT max(total_order_cost)
        FROM daily_total_orders
    )