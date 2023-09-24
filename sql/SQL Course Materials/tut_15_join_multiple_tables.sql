use sql_invoicing;

select p.*, c.name, pm.name as pyt_method
from payments p
join clients c
	on p.client_id = c.client_id
join invoices i
	on p.invoice_id = i.invoice_id
join payment_methods pm
	on p.payment_method = pm.payment_method_id