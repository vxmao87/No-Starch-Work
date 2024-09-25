-- 8-1
select lower("E.E");

-- 8-2
select now();

help 'data types';

create database music;

use music;

create table genre_stream
	(
	genre	varchar(100),
	stream	int
	);
	
insert into genre_stream
	(
	genre,
	stream
	)
values
	('R&B, Hip Hop', 		3102456),
	('Rock',				1577569),
	('Pop',					1298756),
	('Country',				764789),
	('Latin',				601758),
	('Dance, Electronic',	308745);
    
-- 8-3
-- Query for # of rows in table
SELECT COUNT(*)
FROM genre_stream;

-- 8-4
-- Find the average of all streams
SELECT AVG(stream)
FROM genre_stream;

create database vacation;

use vacation;

create table theme_park
	(
	country varchar(50),
	state	varchar(50),
	city	varchar(100),
	park  	varchar(100)
	);
	
insert into theme_park
values
	('USA',		'Florida',			'Orlando',				'Disney World'),
	('USA',		'Florida',			'Orlando',				'Universal Studios'),
	('USA',		'Florida',			'Orlando',				'SeaWorld'),
	('USA',		'Florida',			'Tampa',				'Busch Gardens'),
	('Brazil',	'Santa Catarina',	'Balneario Camboriu',	'Unipraias Park'),
	('Brazil',	'Santa Catarina',	'Florianopolis',		'Show Water Park');
    
-- 8-5
-- Write a query to select country and count of parks in each country
SELECT country,
	   count(park)
FROM theme_park
GROUP BY country;

-- 8-6 
create database mail;

use mail;

create table address(zip_code varchar(20));

insert into address values (94103);
insert into address values (37188);
insert into address values (96718);

SELECT zip_code,
	   SUBSTRING(zip_code, 1, 1) AS national_area,
	   SUBSTRING(zip_code, 2, 2) AS sectional_center,
       SUBSTRING(zip_code, 4, 2) AS associate_post_office
FROM address;

-- 8-7
-- Find time difference between July 23, 2032 and today's date
SELECT DATEDIFF('2032-07-23', CURDATE()) AS time_difference;

-- 8-8
-- Convert 252,088 mi to km and round to nearest km
SELECT ROUND(252088 * 1.60934, 5);

-- 8-9
create database electricity;

use electricity;

create table electrician (
	name varchar(100), 
	years_experience int
	);

insert into electrician 
	(
	name,
	years_experience
	)
values 
	('Zach Zap', 1),
	('Wanda Wiring', 6),
	('Larry Light', 21);
    
-- Ther following query below is incorrect:
-- SELECT name,
-- CASE
-- 	WHEN years_experience < 10 THEN 'Apprentice'
--     WHEN years_experience < 5 THEN 'Journeyman'
--     ELSE 'Master Electrician'
-- END
-- FROM electrician;

-- It should be corrected like this:
SELECT name,
CASE
	WHEN years_experience BETWEEN 5 AND 10 THEN 'Apprentice'
    WHEN years_experience < 5 THEN 'Journeyman'
    ELSE 'Master Electrician'
END
FROM electrician;
