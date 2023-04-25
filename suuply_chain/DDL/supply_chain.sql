-- DDL for supply_chain
-- ---------------------------------------------------------------------------------------

-- Create Schema
create schema supply_chain;
ALTER SCHEMA supply_chain OWNER TO tinitiate;
set search_path = "supply_chain";

delete table suppliers 

CREATE TABLE suppliers(
  supplier_id 		int
  ,name 			VARCHAR(200)
  ,email 			VARCHAR(200)
  ,phone_number 	bigint
  ,address 			VARCHAR(200)
  ,city 			VARCHAR(100)
  ,state 			VARCHAR(100)
  ,zip_code			int
);
alter table suppliers add constraint pk_supplier_id primary key(supplier_id);
ALTER TABLE suppliers ALTER COLUMN phone_number TYPE BIGINT;

select * from suppliers s 


CREATE TABLE orders(
  order_id 					INT
  ,supplier_id 				INT
  ,order_date 				DATE 
  ,expected_delivery_date 	DATE
  ,total_cost 				DECIMAL(10,2)
 );
alter table orders add constraint pk_order_id primary key(order_id);
alter table orders add constraint fk_supplier_id  FOREIGN KEY (supplier_id) REFERENCES suppliers(supplier_id);
alter table orders alter column total_cost type DECIMAL(10,2)

select * from orders o 


CREATE TABLE order_items(
  order_item_id 			INT
  ,order_id					INT 
  ,product_name				VARCHAR(200)
  ,quantity 				INT
  ,unit_price 				DECIMAL
  );
 
alter table order_items add constraint pk_order_item_id primary key(order_item_id);
alter table order_items add constraint fk_order_id FOREIGN KEY (order_id) REFERENCES orders(order_id);

select * from order_items 


CREATE TABLE shipments(
  shipment_id 				INT 
  ,order_id 				INT
  ,shipment_date 			DATE 
  ,carrier_name 			VARCHAR(200) 
  ,tracking_number 			VARCHAR(200) 
  );

alter table shipments add constraint pk_shipment_id primary key(shipment_id);
alter table shipments add constraint fk_order_id FOREIGN KEY (order_id) REFERENCES orders(order_id);
ALTER TABLE shipments ALTER COLUMN shipment_id TYPE BIGINT;

select * from shipments 


CREATE TABLE shipment_items(
  shipment_item_id 			INT
  ,shipment_id 				INT
  ,product_name 			VARCHAR(200)
  ,quantity_received 		INT 
  ,unit_price 				DECIMAL
  );
 
alter table shipment_items add constraint pk_shipment_item_id primary key(shipment_item_id);
alter table shipment_items add constraint fk_shipment_id  FOREIGN KEY (shipment_id) REFERENCES shipments(shipment_id);

select * from shipment_items 


CREATE TABLE payments(
  payment_id 				INT 
  ,supplier_id 				INT 
  ,payment_date 			DATE
  ,payment_method 			VARCHAR(200) 
  ,amount 					DECIMAL
  );
 
alter table payments add constraint pk_payment_id primary key(payment_id);
alter table payments add constraint fk_supplier_id  FOREIGN KEY (supplier_id) REFERENCES suppliers(supplier_id)

select * from payments 









