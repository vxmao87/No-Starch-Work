create database diet;

use diet;

create table calorie
	(
	food			varchar(100),
	calorie_count	int
	);
	
insert into calorie
	(
	food,
	calorie_count
	)
values
	('banana', 110),
	('pizza', 700),
	('apple', 185);
    
-- 11-1
-- NOTE: when running these commands, no need to run the DELIMITER lines, just
-- run the code you want that ends at the new delimiter you chose!
DROP FUNCTION IF EXISTS f_get_calorie_count;
DELIMITER //

CREATE FUNCTION f_get_calorie_count(
	food_param varchar(100)
)
RETURNS INT
DETERMINISTIC READS SQL DATA
BEGIN
	DECLARE calorie_count_var INT;
    SELECT calorie_count
    INTO calorie_count_var
    FROM calorie
    WHERE food = food_param;
    RETURN(calorie_count_var);
END //

DELIMITER ;
SELECT * FROM calorie;
SELECT f_get_calorie_count('pizza');
DROP TABLE calorie;

-- 11-2
create database age;

use age;

create table family_member_age
	(
	person	varchar(100),
	age		int
	);
	
insert into family_member_age
values
('Junior',	7),
('Ricky',	16),
('Grandpa',	102);

DROP PROCEDURE IF EXISTS p_get_age_group;

DELIMITER //

CREATE PROCEDURE p_get_age_group(
	IN person_param varchar(50)
)
BEGIN
	DECLARE age_var INT;
    
	SELECT age
    INTO age_var
    FROM family_member_age
    WHERE person = person_param;
    
    CASE
		WHEN (age_var < 13) THEN SELECT 'Child';
        WHEN (age_var BETWEEN 13 AND 20) THEN SELECT 'Teenager';
        ELSE SELECT 'Adult';
	END CASE;
END //

DELIMITER ;

CALL p_get_age_group('Junior');
CALL p_get_age_group('Ricky');
CALL p_get_age_group('Grandpa');

-- 11-3
DELIMITER //

CREATE PROCEDURE p_get_food()
BEGIN
	SELECT food, calorie_count
    FROM calorie
	ORDER BY calorie_count DESC;
END//

DELIMiTER ;

CALL p_get_food();
