/*https://leetcode.com/problems/customer-who-visited-but-did-not-make-any-transactions/description*/
select customer_id,
    count(customer_id) as count_no_trans
from Visits as v
    left join Transactions as t on v.visit_id = t.visit_id
where transaction_id is null
group by customer_id