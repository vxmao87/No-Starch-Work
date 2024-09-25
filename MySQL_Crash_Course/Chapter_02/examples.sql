create database example;

use example;

create table continent
(
	continent_id	int,
    continent_name	varchar(20),
    population		bigint
);

show databases;

create table customer
(
	customer_id	int,
    first_name	varchar(50),
    last_name	varchar(50),
    address		varchar(150),
    primary key (customer_id)
);

create table high_temperature
(
	city				varchar(50),
    year				int,
    high_temperature	int,
    primary key city, year)
);

create table complaint
(
	complaint_id	int,
    customer_id		int,
    complaint		varchar(500),
    primary key (complaint_id),
    foreign key (customer_id) references customer(customer_id)
);

drop table contact;

create table contact
(
	contact_id		int,
    name			varchar(50) not null,
    city			varchar(50),
    birth_year		int,
    phone			varchar(20),
    email_address	varchar(50) unique,
    constraint check (birth_year between 1900 and 2010),
    primary key (contact_id)
);

drop table high_temperature;

create table high_temperature
(
	city				varchar(50),
    year				int,
    high_temperature	int,
    constraint check (year between 1800 and 2200),
    constraint check (high_temperature < 200),
    primary key (city, year)
);

create table job
(
	job_id		int,
    job_desc	varchar(100),
    shift		varchar(50) default '9-5',
    primary key (job_id)
);

create table product
(
	product_id		int,
    product_name	varchar(100),
    supplier_id		int
);

create index product_supplier_index on product(supplier_id);

show indexes from product;

alter table customer add column zip varchar(50);
alter table customer drop column address;
alter table customer rename column zip to zip_code;
alter table customer rename to valued_customer;

drop database example;

show databases;