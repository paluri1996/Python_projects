import psycopg2
import csv

def load_suppliers_data_csv():
    conn = psycopg2.connect(
            host="127.0.0.1",
            database="tinitiate",
            user="tinitiate",
            password="tinitiate")

    cursor= conn.cursor()
    path = "C:\\Users\\rakes\\Python_practice\\suuply_chain\\data"

    with open(path+'\\suppliers.csv', 'r') as csv_file:
        data = csv.DictReader(csv_file)
        # print(data) 

        for row in data:
            # print(row)
            l_supplier_id=row["supplier_id"]
            l_name = row["name"]
            l_email=row['email']  
            l_phone_number=row['phone_number'] 
            l_address=row['address']
            l_city=row["city"]
            l_state = row["state"]
            l_zip_code=row['zip_code']  
            l_suppliers_insert_str="INSERT INTO supply_chain.suppliers(supplier_id,name,email,phone_number,address,city,state,zip_code) VALUES('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}')".format(l_supplier_id, l_name,l_email,l_phone_number,l_address,l_city,l_state,l_zip_code)
            # print(l_suppliers_insert_str)
            cursor.execute(l_suppliers_insert_str)

    conn.commit()
    cursor.close()
    conn.close() 
  
load_suppliers_data_csv()


