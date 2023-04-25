import psycopg2
import csv

def load_compliance_data_csv():
    conn = psycopg2.connect(
            host="127.0.0.1",
            database="tinitiate",
            user="tinitiate",
            password="tinitiate")

    cursor= conn.cursor()
    path = "C:\\Users\\rakes\\Python_practice\\calc_engine\\data\\compliance_data"

    with open(path+'\\compliance_data.csv', 'r') as csv_file:
        data = csv.DictReader(csv_file)
        # print(data) 

        for row in data:
            # print(row)
            l_compliance_id = row["compliance_id"]
            l_customer_id = row["customer_id"]
            l_transaction_id = row["transaction_id"]
            l_transaction_amount= row['transaction_amount']  
            l_transaction_date = row['transaction_date'] 
            l_aml_check_passed = row['aml_check_passed']
            l_kyc_check_passed = row["kyc_check_passed"]
            l_compliance_insert_str = "INSERT INTO calc_engine.customer(compliance_id,customer_id,transaction_id,transaction_amount,transaction_date,aml_check_passed,kyc_check_passed) VALUES('{0}','{1}','{2}','{3}','{4}','{5}','{6}')".format(l_compliance_id,l_customer_id, l_transaction_id,l_transaction_amount,l_transaction_date,l_aml_check_passed,l_kyc_check_passed)
            print(l_compliance_insert_str)
            cursor.execute(l_compliance_insert_str)

    conn.commit()
    cursor.close()
    conn.close() 
  
load_compliance_data_csv()