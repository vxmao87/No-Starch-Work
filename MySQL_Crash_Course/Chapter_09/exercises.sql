-- 9-1
CREATE DATABASE food;
USE food;

CREATE TABLE favorite_meal
(
	meal  VARCHAR(50),
    price NUMERIC(5,2)
);

INSERT INTO favorite_meal
	(
	meal,
    price
	)
VALUES
	('Pizza', 7.22),
    ('Cheeseburger', 8.41),
    ('Salad', 9.57);
    
SELECT * FROM favorite_meal;

-- 9-2
CREATE DATABASE education;
USE education;

CREATE TABLE college
(
	college_name		 VARCHAR(100),
    location			 VARCHAR(50),
    undergrad_enrollment INT
);

INSERT INTO college
	(
	college_name,
    location,
    undergrad_enrollment
	)
VALUES
	('Princeton University', 'New Jersey', 4773),
	('Massachusetts Institute of Technology', 'Massachusetts', 4361),
    ('Oxford University', 'Oxford', 11955);
    
SELECT * FROM college;

-- 9-3
-- Update all values in favorite_meal table to raise prices by 20%
USE food;

SET SQL_SAFE_UPDATES = 0;

UPDATE favorite_meal
SET price = price * 1.2;

SELECT * FROM favorite_meal;

-- 9-4
DELETE FROM favorite_meal
WHERE meal = "Pizza";

SELECT * FROM favorite_meal;

