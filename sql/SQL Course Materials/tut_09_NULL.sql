use sql_store;

select * from orders
where shipped_date is null or shipper_id is NULL