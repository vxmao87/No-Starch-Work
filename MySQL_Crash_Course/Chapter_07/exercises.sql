create database band;

use band;

create table musician
	(
	musician_name	varchar(100),
	phone			varchar(20),
	musician_type	varchar(100)
	);
	
insert into musician values ('Diva DeLuca', 		'615-758-7836', 'Opera Singer');
insert into musician values ('Skeeter Sullivan', 	'629-209-2332', 'Bluegrass Singer');
insert into musician values ('Tex Macaroni', 		'915-789-1721', 'Country Singer');
insert into musician values ('Bronzy Bohannon', 	'212-211-1216', 'Sax Player');

-- 7-1
-- Select all singers from Tennessee (they have area codes 615 and 629)
SELECT *
FROM musician
WHERE musician_type LIKE "%Singer"
AND (phone LIKE "615%" OR phone LIKE "629%");

create database airport; 

use airport;

create table boarding
	(
	passenger_name		varchar(100),
	license_flag		bool,
	student_id_flag		bool,
	soc_sec_card_flag	bool 
	);
	
insert into boarding values ('Frank Flyer', true, false, false);
insert into boarding values ('Rhonda Runway', false, false, true);
insert into boarding values ('Sam Suitcase', false, true, true);
insert into boarding values ('Pam Prepared', true, true, true);
insert into boarding values ('Sally Stowaway', false, false, false);

-- 7-2
-- We want to select people who have a license, along with EITHER a 
-- student ID OR a social security card. The below query is wrong.
-- SELECT *
-- FROM boarding
-- WHERE license_flag IS TRUE
-- AND student_id_flag IS TRUE
-- OR soc_sec_card_flag IS TRUE;

-- To fix the above query, we need to use parentheses to keep the
-- final two statements together:
SELECT *
FROM boarding
WHERE license_flag IS TRUE
AND
(
	student_id_flag IS TRUE
OR  soc_sec_card_flag IS TRUE
);