-- Write a SQL statement to
-- give any customers born before 1990
-- 50 extra points

use sql_store;

update customers
set points = points + 50
where birth_date < '1990-01-01'
;
-- select * from customers;