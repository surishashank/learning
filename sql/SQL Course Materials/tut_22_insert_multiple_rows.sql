use sql_store;

insert into shippers (name)
values 	('Shipper1'),
		('Shipper2'),
		('Shipper3')
;
select * from shippers
;

insert into products (
	name,
    quantity_in_stock,
    unit_price)
values 	('Product1', 10, 1.95),
		('Product2', 10, 1.95),
		('Product3', 10, 1.95)
;

select * from products