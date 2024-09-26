create database corporate;

use corporate;

create table employee
	(
	employee_name	varchar(100),
	department		varchar(50),
	position		varchar(100),
	home_address    varchar(200),
	date_of_birth	date
	);
	
insert into employee values ('Sidney Crumple', 'accounting', 'Accountant', '123 Credit Road', '1997-01-04');
insert into employee values ('Al Ledger', 'accounting', 'Bookkeeper', '2 Revenue Street', '2002-11-22');
insert into employee values ('Bean Counter', 'accounting', 'Manager', '8 Double Entry Place', '1996-04-29');
insert into employee values ('Lois Crumple', 'accounting', 'Accountant', '123 Debit Lane', '2007-08-27');
insert into employee values ('Loretta Hardsell', 'sales', 'Sales Rep', '66 Hawker Street', '2000-07-09');
insert into employee values ('Bob Closer', 'sales', 'Sales Rep', '73 Peddler Way', '1999-02-16');

-- 10-1
-- Create a view that displays everyone in accounting
CREATE VIEW v_employee_accounting AS
SELECT * FROM employee WHERE department = "accounting";

SELECT * FROM v_employee_accounting;

-- 10-2
-- Create a view that displays everyone in sales
CREATE VIEW v_employee_sales AS
SELECT * FROM employee WHERE department = "sales";

SELECT * FROM v_employee_sales;

-- 10-3
-- Create a view that hides home address and DOB columns
CREATE VIEW v_employee_private AS
SELECT employee_name, department, position FROM employee;

SELECT * FROM v_employee_private;
