use sql_store;

SELECT *
FROM customers
WHERE NOT (birth_date > '1991-2-6' OR
	  (points > 1000 AND state = 'VA'))