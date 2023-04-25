import psycopg2
import csv

def load_financial_data_csv():
    conn = psycopg2.connect(
            host="127.0.0.1",
            database="tinitiate",
            user="tinitiate",
            password="tinitiate")

    cursor= conn.cursor()
    path = "C:\\Users\\rakes\\Python_practice\\calc_engine\\data\\financial_data"

    with open(path+'\\financial_data.csv', 'r') as csv_file:
        data = csv.DictReader(csv_file)
        # print(data) 

        for row in data:
            # print(row)
            l_financial_data_id=row["financial_data_id"]
            l_company_id = row["company_id"]
            l_statement_type=row['statement_type']  
            l_period_start=row['period_start'] 
            l_period_end=row['period_end']
            l_total_assets=row["total_assets"]
            l_total_liabilities = row["total_liabilities"]
            l_total_equity=row['total_equity']  
            l_net_income=row['net_income'] 
            l_operating_cash_flow=row['operating_cash_flow']
            l_investing_cash_flow=row['investing_cash_flow'] 
            l_financing_cash_flow=row['financing_cash_flow']
            l_financial_insert_str="INSERT INTO calc_engine.customer(financial_data_id,company_id,statement_type,period_start,period_end,total_assets,total_liabilities,total_equity,net_income,operating_cash_flow,investing_cash_flow,financing_cash_flow) VALUES('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}','{9}','{10}','{11}')".format(l_financial_data_id, l_company_id,l_statement_type,l_period_start,l_period_end,l_total_assets,l_total_liabilities,l_total_equity,l_net_income,l_operating_cash_flow,l_investing_cash_flow,l_financing_cash_flow)
            print(l_financial_insert_str)
            cursor.execute(l_financial_insert_str)

    conn.commit()
    cursor.close()
    conn.close() 
  
load_financial_data_csv()