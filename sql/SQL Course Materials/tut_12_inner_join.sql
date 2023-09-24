select order_id, o.customer_id, first_name, last_name
from orders o
join customers c
	on o.customer_id = c.customer_id
;

select order_id, oi.product_id, p.name, quantity, oi.unit_price
from order_items oi
join products p
	on p.product_id = oi.product_id
    
