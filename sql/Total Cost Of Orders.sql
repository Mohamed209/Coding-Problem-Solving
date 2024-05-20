/*https://platform.stratascratch.com/coding/10183-total-cost-of-orders?code_type=1*/
select sum(total_order_cost) as total_orders_cost,
       first_name
from orders
inner join customers on orders.cust_id = customers.id
group by cust_id,
         first_name
order by first_name