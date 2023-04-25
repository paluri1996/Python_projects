import psycopg2
import os
import csv


def load_customer_data_csv():
    conn = psycopg2.connect(
            host="127.0.0.1",
            database="tinitiate",
            user="tinitiate",
            password="tinitiate")

    cursor= conn.cursor()
    path = "C:\\Users\\rakes\\Python_practice\\calc_engine\\data\\customer_data"

    with open(path+'\\customer_data.csv', 'r') as csv_file:
        data = csv.DictReader(csv_file)
        # print(data) 

        for row in data:
            # print(row)
            l_customer_id=row["customer_id"]
            l_customer_name = row["customer_name"]
            l_account_number=row['account_number']  
            l_account_type=row['account_type'] 
            l_account_balance=row['account_balance'] 
            l_customer_insert_str="INSERT INTO calc_engine.customer(customer_id,customer_name,account_number,account_type,account_balance) VALUES('{0}','{1}','{2}','{3}','{4}')".format(l_customer_id, l_customer_name,l_account_number,l_account_type,l_account_balance)
            print(l_customer_insert_str)
            cursor.execute(l_customer_insert_str)

    
    conn.commit()
    cursor.close()
    conn.close() 
  
load_customer_data_csv()