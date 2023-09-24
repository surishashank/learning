SELECT * FROM sql_store.orders;

update orders o
set o.comments = 'Gold customer'
where o.customer_id IN
				(select customer_id
				 from customers
				 where points > 3000);

select * from orders