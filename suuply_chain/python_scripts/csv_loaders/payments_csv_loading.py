import psycopg2
import csv

def load_payments_csv():
    conn = psycopg2.connect(
            host="127.0.0.1",
            database="tinitiate",
            user="tinitiate",
            password="tinitiate")

    cursor= conn.cursor()
    path = "C:\\Users\\rakes\\Python_practice\\suuply_chain\\data"

    with open(path+'\\payments.csv', 'r') as csv_file:
        data = csv.DictReader(csv_file)
        # print(data) 

        # payment_id,supplier_id,payment_date,payment_method,amount

        for row in data:
            # print(row)
            l_payment_id = row["payment_id"]
            l_supplier_id=row["supplier_id"]
            l_payment_date=row['payment_date']  
            l_payment_method=row['payment_method'] 
            l_amount=row['amount'] 
            l_payments_insert_str="INSERT INTO supply_chain.payments(payment_id,supplier_id,payment_date,payment_method,amount) VALUES('{0}','{1}','{2}','{3}','{4}')".format( l_payment_id,l_supplier_id,l_payment_date,l_payment_method,l_amount)
            # print(l_suppliers_insert_str)
            cursor.execute(l_payments_insert_str)

    conn.commit()
    cursor.close()
    conn.close() 
  
load_payments_csv()