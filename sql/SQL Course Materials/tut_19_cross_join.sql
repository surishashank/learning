use sql_store;

select
	c.first_name as customer,
    p.name AS product
from customers c
cross join products p
order by c.first_name