SELECT *
FROM customers
WHERE last_name	REGEXP 'e[fmlq]|[a-h]e';

-- ^ beginning of string
-- $ end of string
-- | logical or
-- [abcd] match any single character in bracket
-- [a-f] match any single character in range

SELECT * 
FROM customers
WHERE first_name in ('ELKA', 'AMBUR');

select *
from customers
where last_name REGEXP 'EY$|ON$';

select *
from customers
where last_name REGEXP '^MY|SE';

select *
from customers
where last_name REGEXP 'B[RU]';