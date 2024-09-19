/* 2-1 */
show databases;

/* 2-2 */
create database cryptocurrency;

show databases;

/* 2-3 */
drop database cryptocurrency;

show databases; 

/* 2-4 */
create database athletic;
use athletic;

create table sport 
(
	sport_id	int,
    sport_name	varchar(50),
    primary key (sport_id)
);

create table player 
(
	player_id	int,
    player_name	varchar(50),
    player_age	int,
    sport_id	int,
    primary key (player_id),
    foreign key (sport_id) references sport(sport_id)
);

drop database athletic;
show databases;
