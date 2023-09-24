insert into orders (customer_id, order_date, status)
values (1, '2019-01-02', 1);

insert into order_items (order_id, product_id, quantity, unit_price)
values 	(last_insert_id(), 1, 4, 2.99),
		(last_insert_id(), 2, 3, 4.99)