-- 1. Create a database called bootcamp.
-- 2. Create a table called students.
-- 3. Add the following columns:
--    1.id
--    2.last_name
--    3.first_name
--    4.birth_date
--      The id must be auto_incremented.
--      Make sure to choose the correct data type for each column.
--      To help, here is the data that you will have to insert. (How do we insert a date to a table?)

CREATE TABLE students(
 stud_id SERIAL PRIMARY KEY,
 first_name VARCHAR (50) NOT NULL,
 last_name VARCHAR (100) NOT NULL,
 birth_date DATE NOT NULL
);

-- Here is the data:
--
-- id	first_name	last_name	birth_date
-- 1	Marc	Benichou	02/11/1998
-- 2	Yoan	Cohen	03/12/2010
-- 3	Lea	Benichou	27/07/1987
-- 4	Amelia	Dux	07/04/1996
-- 5	David	Grez	14/06/2003
-- 6	Omer	Simpson	03/10/1980
--
--
-- Insert
--   1. Insert the data seen above to the students table. Find the most efficient way to insert the data.
insert into students (first_name, last_name, birth_date) values
('Marc', 'Benichou', '02/11/1998'),
('Yoan', 'Cohen', '03/12/2010'),
('Lea',	'Benichou',	'27/07/1987'),
('Amelia', 'Dux', '07/04/1996'),
('David', 'Grez', '14/06/2003'),
('Omer', 'Simpson',	'03/10/1980') ;
--   2. Insert your last_name, first_name and birth_date to the students table (Take a look at the id given).
insert into students (first_name, last_name, birth_date) values
('Alexander', 'Replyansky', '20/08/94') ;

-- Select
-- 1. Fetch all of the data from the table.
select * from students;
-- 2. Fetch all of the students first_names and last_names.
select first_name, last_name from students;
-- 3. For the following questions, only fetch the first_names and last_names of the students.
--    1. Fetch the student which id is equal to 2.
select * from students where stud_id = 2;
-- 	  2. Fetch the student whose last_name is Benichou AND first_name is Marc.
select * from students where last_name = 'Benichou' and first_name = 'Marc';
-- 	  3. Fetch the students whose last_names are Benichou OR first_names are Marc.
select * from students where last_name = 'Benichou' or first_name = 'Marc';
--    4. Fetch the students whose first_names contain the letter a.
select * from students where first_name like '%a%' ;
-- 	  5. Fetch the students whose first_names start with the letter a.
select * from students where first_name ilike 'a%' ;
--    6. Fetch the students whose first_names end with the letter a.
select * from students where first_name like '%a' ;
--    7. Fetch the students whose second to last letter of their first_names are a (Example: Leah).
select * from students where first_name like '%_a_%' ;
-- 	  8. Fetch the students whose id’s are equal to 1 AND 3 .
select * from students where stud_id = 1 or stud_id = 3 ;
-- 4. Fetch the students whose birth_dates are equal to or come after 1/01/2000. (show all their info).
select * from students where birth_date >= '1/01/2000' ;
