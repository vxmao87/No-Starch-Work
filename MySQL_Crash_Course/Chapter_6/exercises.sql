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