USE sql_store;

SELECT *
FROM products
WHERE quantity_in_stock IN (49, 38, 72)