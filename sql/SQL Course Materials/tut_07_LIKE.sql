USE sql_store;

-- Get the customers whose
-- 	addresses contain TRAIL or AVENUE
--  OR
-- 	phone numbers end with 9

SELECT *
FROM customers
WHERE address LIKE '%TRAIL%' OR 
	  address LIKE '%AVENUE%' OR
	  phone LIKE '%9'
