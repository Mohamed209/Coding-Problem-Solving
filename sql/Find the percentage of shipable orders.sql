/*https://platform.stratascratch.com/coding/10090-find-the-percentage-of-shipable-orders?code_type=1*/
select 100 *(
        sum(
            case
                when address != '' then 1
                else 0
            end
        ) / cast(count(orders.id) as float)
    ) as percent_shipable
from orders
    inner join customers on orders.cust_id = customers.id