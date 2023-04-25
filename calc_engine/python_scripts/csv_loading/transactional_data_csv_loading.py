import psycopg2
import csv

def load_transaction_data_csv():
    conn = psycopg2.connect(
            host="127.0.0.1",
            database="tinitiate",
            user="tinitiate",
            password="tinitiate")

    cursor= conn.cursor()
    path = "C:\\Users\\rakes\\Python_practice\\calc_engine\\data\\trasaction_data"

    with open(path+'\\transaction_data.csv', 'r') as csv_file:
        data = csv.DictReader(csv_file)
        # print(data) 

        for row in data:
            # print(row)
            l_transaction_id=row["transaction_id"]
            l_customer_id = row["customer_id"]
            l_deposit_amount=row['deposit_amount']  
            l_withdrawal_amount=row['withdrawal_amount'] 
            l_transfer_amount=row['transfer_amount']
            l_transaction_date=row['transaction_date']
            l_transaction_insert_str="INSERT INTO calc_engine.transaction_data(transaction_id,customer_id,deposit_amount,withdrawal_amount,transfer_amount,transaction_date) VALUES('{0}','{1}','{2}','{3}','{4}','{5}')".format(l_transaction_id, l_customer_id,l_deposit_amount,l_withdrawal_amount,l_transfer_amount,l_transaction_date)
            print(l_transaction_insert_str)
            cursor.execute(l_transaction_insert_str)

    conn.commit()
    cursor.close()
    conn.close() 
  
load_transaction_data_csv()