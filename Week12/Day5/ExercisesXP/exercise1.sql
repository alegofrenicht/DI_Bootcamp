-- 🌟 Exercise 1 : Items And Customers
-- Instructions
-- We will work on the public database that we created yesterday.
CREATE TABLE items(
 item_id SERIAL PRIMARY KEY,
 desk_type VARCHAR (50) NOT NULL,
 price  SMALLINT NOT NULL
);

insert into items (desk_type, price) values
('Small Desk', 100),
('Big Desk', 300),
('Fan', 80);


CREATE TABLE customers(
 item_id SERIAL PRIMARY KEY,
 cust_name VARCHAR (50) NOT NULL,
 cust_lastname  VARCHAR (50) NOT NULL
);

insert into customers (cust_name, cust_lastname) values
('Greg', 'Jones'),
('Sandra', 'Jones'),
('Scott', 'Scott'),
('Trevor', 'Green'),
('Melanie', 'Johnson');

--
-- Use SQL to get the following from the database:
-- All items, ordered by price (lowest to highest).
select * from items order by price;
-- Items with a price above 80 (80 included), ordered by price (highest to lowest).
select * from items where price >= 80 order by price desc;
-- The first 3 customers in alphabetical order of the first name (A-Z) – exclude the primary key column from the results.
select cust_name, cust_lastname from customers order by cust_name limit 3;
-- All last names (no other columns!), in reverse alphabetical order (Z-A)
select cust_lastname from customers order by cust_lastname desc


