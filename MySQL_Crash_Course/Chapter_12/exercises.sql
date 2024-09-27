-- 12-1
create database jail;

use jail;

create table alcatraz_prisoner
	(
	prisoner_id		int,
	prisoner_name	varchar(100)
	);
	
insert into alcatraz_prisoner
	(
	prisoner_id,
	prisoner_name
	)
values
	(85,	'Al Capone'),
	(594,	'Robert Stroud'),
	(1476, 	'John Anglin');
    
-- create an audit table for 12-1
CREATE TABLE alcatraz_prisoner_audit
	(
		audit_datetime	DATETIME,
        audit_user		VARCHAR(100),
        audit_change	VARCHAR(500)
    );
    
-- 12-2
-- Write a trigger for the table above
DROP TRIGGER IF EXISTS tr_alcatraz_prisoner_ai;

DELIMITER //

CREATE TRIGGER tr_alcatraz_prisoner_ai
	AFTER INSERT ON alcatraz_prisoner
    FOR EACH ROW
    BEGIN
		INSERT INTO alcatraz_prisoner_audit
			(
				audit_datetime,
				audit_user,
				audit_change
            )
		VALUES
			(
				NOW(),
                USER(),
                CONCAT(
					'New row for prisoner_id ',
					NEW.prisoner_id,
					'. Prisoner Name: ',
					NEW.prisoner_name
				)
            );
	END //
    
DELIMITER ;
INSERT INTO alcatraz_prisoner
	(
		prisoner_id,
        prisoner_name
    )
VALUES 
	(
		117,
        "Machine Gun Kelly"
    );
    
SELECT * FROM alcatraz_prisoner_audit;
DROP DATABASE IF EXISTS jail;

-- 12-3
create database exam;

use exam;

create table grade
	(
	student_name	varchar(100),
	score 			int
	);
	
insert into grade
	(
	student_name,
	score
	)
values
	('Billy',79),
	('Jane', 87),
	('Paul', 93);
    
-- Create a before-update trigger for this table
DROP TRIGGER IF EXISTS tr_grade_bu;
DELIMITER //

CREATE TRIGGER tr_grade_bu
	BEFORE UPDATE ON grade
    FOR EACH ROW
    BEGIN
		IF (NEW.score < 50) THEN
			SET NEW.score = 50;
		END IF;
        
		IF (NEW.score > 100) THEN
			SET NEW.score = 100;
		END IF;
	END //
    
DELIMITER ;

SET SQL_SAFE_UPDATES = 0;    
UPDATE grade SET SCORE = 38 WHERE student_name = "Billy";
UPDATE grade SET SCORE = 107 WHERE student_name = "Jane";
UPDATE grade SET SCORE = 95 WHERE student_name = "Paul";

SELECT * FROM grade;
