use sql_invoicing;

select
	p.date,
    c.name as client,
    p.amount,
    pm.name as payment_method
from payments p
left join clients c using (client_id)
left join payment_methods pm
	on p.payment_method = pm.payment_method_id
