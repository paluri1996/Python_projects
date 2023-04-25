import psycopg2
import os
import csv

def load_operational_data_csv():
    conn = psycopg2.connect(
            host="127.0.0.1",
            database="tinitiate",
            user="tinitiate",
            password="tinitiate")

    cursor= conn.cursor()
    path = "C:\\Users\\rakes\\Python_practice\\calc_engine\\data\\operational_data"

    with open(path+'\\operational_data.csv', 'r') as csv_file:
        data = csv.DictReader(csv_file)
        # print(data) 

        for row in data:
            # print(row)
            l_operational_id = row["operational_id"]
            l_customer_id = row["customer_id"]
            l_supplier_id = row["supplier_id"]
            l_transaction_date = row['transaction_date']  
            l_transaction_type = row['transaction_type'] 
            l_quantity = row['quantity'] 
            l_price = row['price'] 
            l_operational_insert_str="INSERT INTO calc_engine.operational_data(operational_id,customer_id,supplier_id,transaction_date,transaction_type,quantity,price) VALUES('{0}','{1}','{2}','{3}','{4}','{5}','{6}')".format(l_operational_id,l_customer_id, l_supplier_id,l_transaction_date,l_transaction_type,l_quantity,l_price)
            print(l_operational_insert_str)
            cursor.execute(l_operational_insert_str)

    conn.commit()
    cursor.close()
    conn.close() 
  
load_operational_data_csv()