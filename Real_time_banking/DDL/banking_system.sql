-- DDL for banking_system
-- ---------------------------------------------------------------------------------------

-- Create Schema


--
create schema banking_system;
ALTER SCHEMA banking_system OWNER TO tinitiate;
set search_path = "banking_system";




-- creating customer table

create table customer(
customer_id				int
,customer_name			varchar(100)
,account_number			int
,account_type			varchar(100)
,account_balance		int
);

alter table customer add constraint pk_customer_id primary key(customer_id)


select * from banking_system.customer 
delete from banking_system.customer

