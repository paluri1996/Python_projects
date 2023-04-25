import json
import psycopg2
import os

def load_bank_records_json():
       #connection
    conn = psycopg2.connect(
            host="127.0.0.1",
            database="tinitiate",
            user="tinitiate",
            password="tinitiate")

    cursor= conn.cursor()

    path = "C:\\Users\\rakes\\Python_practice\\Real_time_banking\\data"
    for filename in os.listdir(path):
        if filename.endswith(".json"):
            inputfile = os.path.join(path, filename)
            print(inputfile)
            with open(inputfile,'r') as f:    
                data = json.load(f)

                l_seq=1
                for row in data:
                    l_customer_id=row["customer_id"]
                    l_customer_name = row["customer_name"]
                    l_account_number=row['account_number']  
                    l_account_type=row['account_type'] 
                    l_account_balance=row['account_balance'] 
                    l_customer_insert_str="INSERT INTO banking_system.customer(customer_id,customer_name,account_number,account_type,account_balance) VALUES('{0}','{1}','{2}','{3}','{4}')".format(l_customer_id, l_customer_name,l_account_number,l_account_type,l_account_balance)
                    cursor.execute(l_customer_insert_str)
    conn.commit()
    cursor.close()
    conn.close() 

load_bank_records_json()           
                