-- drop table orders;
-- drop table employees;
-- drop table customers;



create table employees
(
	employee_id int primary key,
	first_name varchar(128) not null,
	last_name varchar(128) not null,
	title varchar(40) not null,
	birth_date date not null,
	notes text
);

create table customers
(
	customer_id varchar(5) primary key not null,
	company_name varchar(128),
	contact_name varchar(128)
);

create table orders
(
	order_id int primary key,
	customer_id varchar(5),
	employee_id int references employees(employee_id) not null,
	order_date date not null,
	ship_city varchar(128)
);