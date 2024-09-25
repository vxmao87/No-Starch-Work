create database if not exists solar_system;

use solar_system;

create table planet
	(
	planet_id     int,
	planet_name   varchar(50)
	);
	
create table ring
	(
	planet_id    int,
	ring_tot     int
	);
	
insert into planet (planet_id, planet_name)
values
(1, 'Mercury'),
(2, 'Venus'),
(3, 'Earth'),
(4, 'Mars'),
(5, 'Jupiter'),
(6, 'Saturn'),
(7, 'Uranus'),
(8, 'Neptune');
	
insert into ring (planet_id, ring_tot)
values 
(5, 3),
(6, 7),
(7, 13),
(8, 6);

-- 5-1 (inner join on both tables using planet_id)
select p.planet_id, p.planet_name, r.ring_tot
from planet as p
inner join ring as r
on p.planet_id = r.planet_id;

-- 5-2 (outer join with planet as left table)
select p.planet_id, p.planet_name, r.ring_tot
from planet as p left outer join ring as r
using (planet_id);

-- 5-3 (outer join with planet as right table, answer must be the same as 5-2)
select p.planet_id, p.planet_name, r.ring_tot
from ring as r right outer join planet as p
using (planet_id);

-- 5-4 (use column alias on r.ring_tot)
select p.planet_id,
	   p.planet_name, 
       r.ring_tot as rings
from ring as r right outer join planet as p
using (planet_id);

drop database if exists solar_system;
