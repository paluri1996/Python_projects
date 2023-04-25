-- DDL for calc_engine
-- ---------------------------------------------------------------------------------------

-- Create Schema
create schema calc_engine;
ALTER SCHEMA calc_engine OWNER TO tinitiate;
set search_path = "calc_engine";



---- customer_data----
create table customer(
customer_id				int
,customer_name			varchar(100)
,account_number			int
,account_type			varchar(100)
,account_balance		int
);

alter table customer add constraint pk_customer_id primary key(customer_id)
-- select statement 
select * from calc_engine.customer



---- transaction_data----
create table transaction_data(
transaction_id			int
,customer_id			int
,deposit_amount			DECIMAL
,withdrawal_amount		DECIMAL
,transfer_amount		DECIMAL
,transaction_date		Date
);

alter table transaction_data add constraint pk_transaction_id primary key(transaction_id);
alter table transaction_data add constraint fk_customer_id foreign key(customer_id) references customer(customer_id);

select * from calc_engine.transaction_data


---- market_data----
CREATE TABLE market_data(
market_data_id		int
,market_trend		varchar(100)
,economic_indicator	varchar(100)
,external_factor	varchar(100)
,value				FLOAT
);

alter table market_data add constraint pk_market_data_id primary key(market_data_id);

select * from calc_engine.market_data



---- operational_data----
CREATE TABLE operational_data(
operational_id		    int
,customer_id			int
,supplier_id 			int
,transaction_date		TIMESTAMP
,transaction_type		varchar(100)
,quantity				int
,price					DECIMAL(10,2)
);


alter table operational_data add constraint pk_operational_id primary key(operational_id);
alter table operational_data add constraint fk_customer_id foreign key(customer_id) references customer(customer_id);
--- alter table operational_data add constraint fk_transaction_date foreign key(transaction_date) references transaction_data(transaction_date);

select * from calc_engine.operational_data



---- compliance_data----
CREATE TABLE compliance_data(
compliance_data_id		int
,customer_id			int
,transaction_id 		int
,transaction_amount		DECIMAL(10,2)
,transaction_date 		timestamp
,aml_check_passed 		BOOLEAN
,kyc_check_passed 		BOOLEAN
);

alter table compliance_data add constraint pk_compliance_data_id primary key(compliance_data_id);
alter table operational_data add constraint fk_customer_id foreign key(customer_id) references customer(customer_id);
alter table operational_data add constraint fk_transaction_id foreign key(transaction_id) references transaction_data(transaction_id);
--- alter table operational_data add constraint fk_transaction_date foreign key(transaction_date) references transaction_data(transaction_date);

select * from calc_engine.compliance_data



---- risk_data----
CREATE TABLE risk_data(
risk_data_id		 int
,customer_id		 int
,product_id 		 int
,credit_score 		 int
,default_probability DECIMAL(10,2)
,market_value		 DECIMAL(10,2)
,volatility 		 DECIMAL(10,2)
,operational_loss	 DECIMAL(10,2)
);

alter table risk_data add constraint pk_risk_data_id primary key(risk_data_id);
alter table operational_data add constraint fk_customer_id foreign key(customer_id) references customer(customer_id);

select * from calc_engine.risk_data


---- financial_data----
CREATE TABLE financial_data(
financial_data_id		 int
,company_id 			 int
,statement_type 		 TEXT
,period_start 			 DATE
,period_end				 DATE
,total_assets 			 DECIMAL(15,2)
,total_liabilities       DECIMAL(15,2)
,total_equity            DECIMAL(15,2)
,net_income              DECIMAL(15,2)
,operating_cash_flow     DECIMAL(15,2)
,investing_cash_flow     DECIMAL(15,2)
,financing_cash_flow     DECIMAL(15,2)
);

alter table financial_data add constraint pk_financial_data_id primary key(financial_data_id);

select * from calc_engine.financial_data