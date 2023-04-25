-- DDL for Billing project
-- ---------------------------------------------------------------------------------------

-- Create Schema
--
create schema data_loading;
ALTER SCHEMA data_loading OWNER TO tinitiate;
set search_path = "data_loading";

-- Products Table
--
drop table products;
--
create table products(
product_id			int NOT NULL
,product_name		varchar(100)
,product_price		NUMERIC(7,2)
,product_category	varchar(200)
);

alter table products add constraint pk_products primary key (product_id);


-- Bills Table
-- drop table bills
create table bills(
bill_id				int
,bill_date 			TIMESTAMP
,store_id			int
,bill_total         decimal
);

alter table bills add constraint pk_bills primary key (bill_id);

-- Bill Details Table
-- 
drop table data_loading.bill_details;
--
create table data_loading.bill_details(
bill_detail_id 		varchar(100)
,bill_id			int
,quantity           decimal
,product_id			int 
);

alter table data_loading.bill_details add constraint pk_bill_details primary key (bill_detail_id);
alter table data_loading.bill_details add constraint fk_bill_details foreign key (bill_id) references bills(bill_id);
alter table data_loading.bill_details add constraint fk_bill_details_prod_id foreign key (product_id) references products(product_id);


-- Queries
-- 
-- Delete all Rows
delete from products 
delete from bills 
delete from bill_details  

-- Queries for bills table
select * from bills 
select max(bill_id) from bills
select count(*) from bills

select * from bill_details

-- Queries for products table
select * from products
select count(*) from products
select max(product_id) from products
select max(product_price) from products

select * 
from  products 
where product_price = (select max(product_price) from products)

select * from products

delete from products 


select * from bills
select * from bill_details bd 

delete from bills

-- Joining bills and bill details for a specific bill_id
select 	* 
from    bills b , bill_details bd 
where 	b.bill_id = bd.bill_id 
and 	b.bill_id = 10009
