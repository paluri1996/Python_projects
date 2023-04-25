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
