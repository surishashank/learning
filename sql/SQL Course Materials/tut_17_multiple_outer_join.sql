use sql_store;

select
	c.customer_id,
    c.first_name,
    o.order_id,
    o.shipper_id,
    sh.name AS shipper
from customers c
left join orders o 
	on c.customer_id = o.customer_id
left join shippers sh
	on o.shipper_id = sh.shipper_id
order by c.customer_id
;

select
	o.order_date,
    o.order_id,
    c.first_name as customer,
    s.name as shipper,
    os.name as status
from orders o
left join customers c
	on o.customer_id = c.customer_id
left join shippers s
	on o.shipper_id = s.shipper_id
left join order_statuses os
	on o.status = os.order_status_id


-- select
-- 	p.product_id,
--     p.name,
--     oi.quantity
-- from products p 
-- left join order_items oi
-- 	on p.product_id = oi.product_id

-- select *
-- from customers
