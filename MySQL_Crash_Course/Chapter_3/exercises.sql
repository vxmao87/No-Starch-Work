create database if not exists feedback;

use feedback;

drop table if exists customer;

create table customer
(
    customer_id     int,
    first_name	    varchar(50),
    last_name       varchar(50),
    address         varchar(100),
    primary key (customer_id)
); 

insert into customer (customer_id, first_name, last_name, address)
values
(1, 'Bob', 'Smith', '12 Dreary Lane'),
(2, 'Sally', 'Jones', '76 Boulevard Meugler'),
(3, 'Karen', 'Bellyacher', '354 Main Street');

-- 3-1
select first_name, last_name from customer;

-- 3-2
select customer_id, first_name, last_name
from customer
where first_name = "Karen";