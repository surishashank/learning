use sql_invoicing;

-- select client_id
-- from clients
-- where name = 'MyWoRKs'

delete from invoices
where client_id = (
			select client_id
            from clients
            where name = 'Myworks'
            );

select * from invoices