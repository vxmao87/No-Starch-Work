CREATE DATABASE IF NOT EXISTS nutrition;

USE nutrition;

CREATE TABLE good_snack
(
	snack_name	varchar(50)
);

CREATE TABLE bad_snack
(
	snack_name	varchar(50)
);

INSERT INTO good_snack(snack_name)
VALUES
('carrots'),
('salad'),
('soup');

INSERT INTO bad_snack(snack_name)
VALUES
('sausage pizza'),
('BBQ ribs'),
('nachos');

-- 6-1
SELECT snack_name from good_snack
UNION
SELECT snack_name from bad_snack;

DROP DATABASE IF EXISTS nutrition;

create database canada;

use canada;

create table province
	(
	province_id			int,
	province_name		varchar(100),
	official_language	varchar(20)
);
	
insert into province (province_id, province_name, official_language) values (1, 'Alberta', 'English');
insert into province (province_id, province_name, official_language) values (2, 'British Columbia', 'English');
insert into province (province_id, province_name, official_language) values (3, 'Manitoba', 'English');
insert into province (province_id, province_name, official_language) values (4, 'New Brunswick', 'English, French');
insert into province (province_id, province_name, official_language) values (5, 'Newfoundland', 'English');
insert into province (province_id, province_name, official_language) values (6, 'Nova Scotia', 'English');
insert into province (province_id, province_name, official_language) values (7, 'Ontario', 'English');
insert into province (province_id, province_name, official_language) values (8, 'Prince Edward Island', 'English'); 
insert into province (province_id, province_name, official_language) values (9, 'Quebec', 'French');
insert into province (province_id, province_name, official_language) values (10, 'Saskatchewan', 'English');

create table capital_city
	(
	city_id		int,
	city_name	varchar(100),
	province_id	int
	);

insert into capital_city (city_id, city_name, province_id) values (1, 'Toronto', 7);
insert into capital_city (city_id, city_name, province_id) values (2, 'Quebec City', 9);
insert into capital_city (city_id, city_name, province_id) values (3, 'Halifax', 5);
insert into capital_city (city_id, city_name, province_id) values (4, 'Fredericton', 4);
insert into capital_city (city_id, city_name, province_id) values (5, 'Winnipeg', 3);
insert into capital_city (city_id, city_name, province_id) values (6, 'Victoria', 2);
insert into capital_city (city_id, city_name, province_id) values (7, 'Charlottetown', 8);
insert into capital_city (city_id, city_name, province_id) values (8, 'Regina', 10);
insert into capital_city (city_id, city_name, province_id) values (9, 'Edmonton', 1);
insert into capital_city (city_id, city_name, province_id) values (10,'St. Johns', 5);
	
create table tourist_attraction
	(
	attraction_id		int,
	attraction_name		varchar(100),
	attraction_city_id	int,
	open_flag			bool
	);

insert into tourist_attraction (attraction_id, attraction_name, attraction_city_id, open_flag) values (1, 'CN Tower', 1, true);
insert into tourist_attraction (attraction_id, attraction_name, attraction_city_id, open_flag) values (2, 'Old Quebec', 2, true);
insert into tourist_attraction (attraction_id, attraction_name, attraction_city_id, open_flag) values (3, 'Royal Ontario Museum', 1, true);
insert into tourist_attraction (attraction_id, attraction_name, attraction_city_id, open_flag) values (4, 'Place Royale', 2, true);
insert into tourist_attraction (attraction_id, attraction_name, attraction_city_id, open_flag) values (5, 'Halifax Citadel', 3, true);
insert into tourist_attraction (attraction_id, attraction_name, attraction_city_id, open_flag) values (6, 'Garrison District', 4, true);
insert into tourist_attraction (attraction_id, attraction_name, attraction_city_id, open_flag) values (7, 'Confederation Centre of the Arts', 7, true);
insert into tourist_attraction (attraction_id, attraction_name, attraction_city_id, open_flag) values (8, 'Stone Hall Castle', 8, true);
insert into tourist_attraction (attraction_id, attraction_name, attraction_city_id, open_flag) values (9, 'West Edmonton Mall', 9, true);
insert into tourist_attraction (attraction_id, attraction_name, attraction_city_id, open_flag) values (10,'Signal Hill', 10, true);
insert into tourist_attraction (attraction_id, attraction_name, attraction_city_id, open_flag) values (11,'Canadian Museum for Human Rights', 5, true);
insert into tourist_attraction (attraction_id, attraction_name, attraction_city_id, open_flag) values (12,'Royal BC Museum', 6, true);
insert into tourist_attraction (attraction_id, attraction_name, attraction_city_id, open_flag) values (13,'Sunnyside Amusement Park', 1, false);

-- 6-2
-- Join the three tables above by:
-- - Selecting the attraction_city column from the tourist_attraction table
-- - Selecting the city_name column the capital_city table
-- - Selecting the province_name column from the province table
-- - Selecting rows from the attraction table where open_flag = True
-- - Selecting rows from the province table where official_language is French
SELECT t.attraction_name,
	   c.city_name,
       p.province_name
FROM province p
JOIN capital_city c
ON p.province_id = c.province_id
AND p.official_language = "French"
JOIN tourist_attraction t
ON c.city_id = t.attraction_city_id
AND open_flag IS TRUE;

-- 6-3
-- Creating a temporary table
CREATE TEMPORARY TABLE open_tourist_attraction
SELECT attraction_name,
	   attraction_city_id
FROM tourist_attraction
WHERE open_flag IS TRUE;

SELECT * FROM open_tourist_attraction;

-- 6-4
SELECT o.attraction_name,
	   c.city_name
FROM open_tourist_attraction o
JOIN capital_city c
ON c.city_id = o.attraction_city_id
AND c.city_name = "Toronto";

create database attire;

use attire;

create table employee
	(
	employee_id		int,
	employee_name	varchar(100),
	position_name	varchar(100)
	);
	
insert into employee(employee_id, employee_name, position_name) values (1, 'Benedict', 'Pope');
insert into employee(employee_id, employee_name, position_name) values (2, 'Garth', 'Singer');
insert into employee(employee_id, employee_name, position_name) values (3, 'Francis', 'Pope');

create table wardrobe
	(
	employee_id	int,
	hat_size	numeric(4,2)
	);

insert into wardrobe (employee_id, hat_size) values (1, 8.25);
insert into wardrobe (employee_id, hat_size) values (2, 7.50);
insert into wardrobe (employee_id, hat_size) values (3, 6.75);

-- 6-5
-- SELECT employee_id,
-- 	   hat_size
-- FROM wardrobe
-- WHERE employee_id =
-- (
-- 	SELECT employee_id
--     FROM employee
--     WHERE position_name = "Pope"
-- );
SELECT employee_id,
	   hat_size
FROM wardrobe
WHERE employee_id IN
(
	SELECT employee_id
    FROM employee
    WHERE position_name = "Pope"
);
/*
The query above was fixed by changing '=' ti 'IN'. Because Employee #3 was added recently
before the query was ran again, the error occurred because '=' implies that the subquery
inside the parenthesis can return one and only one row.
*/

create database monarchy;

use monarchy;

create table royal_family
(
	name		varchar(200),
	birthdate	date
);

insert into royal_family (name, birthdate) values ('Prince Louis of Cambridge', '2018-04-23');
insert into royal_family (name, birthdate) values ('Princess Charlotte of Cambridge', '2015-05-02');
insert into royal_family (name, birthdate) values ('Prince George of Cambridge', '2013-07-22');
insert into royal_family (name, birthdate) values ('Prince William, Duke of Cambridge', '1982-06-21');
insert into royal_family (name, birthdate) values ('Catherine, Duchess of Cambridge', '1982-01-09');
insert into royal_family (name, birthdate) values ('Charles, Prince of Whales','1948-11-14');
insert into royal_family (name, birthdate) values ('Queen Elizabeth II', '1926-04-21');
insert into royal_family (name, birthdate) values ('Prince Andrew, Duke of York', '1960-02-19');

-- 6-6
SELECT * FROM royal_family ORDER BY birthdate;

-- 6-7
SELECT * FROM royal_family ORDER BY birthdate LIMIT 1;

-- 6-8
SELECT * FROM royal_family ORDER BY birthdate DESC LIMIT 3;
