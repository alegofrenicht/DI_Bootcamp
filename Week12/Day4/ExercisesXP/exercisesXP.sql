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

select * from items;
select * from items where price > 80;
select * from items where price <= 300;
select * from customers where cust_lastname = 'Smith';
select * from customers where cust_lastname = 'Jones';
select * from customers where cust_lastname != 'Scott';
