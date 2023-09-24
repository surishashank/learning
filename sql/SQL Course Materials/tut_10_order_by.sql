select *, quantity * unit_price as total_price
from order_items
where order_id = 2
order by total_price DESC