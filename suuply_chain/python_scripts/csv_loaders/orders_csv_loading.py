import psycopg2
import csv

def load_orders_data_csv():
    conn = psycopg2.connect(
            host="127.0.0.1",
            database="tinitiate",
            user="tinitiate",
            password="tinitiate")

    cursor= conn.cursor()
    path = "C:\\Users\\rakes\\Python_practice\\suuply_chain\\data"

    with open(path+'\\orders.csv', 'r') as csv_file:
        data = csv.DictReader(csv_file)
        # print(data) 

        for row in data:
            # print(row)
            l_order_id=row["order_id"]
            l_supplier_id = row["supplier_id"]
            l_order_date=row['order_date']  
            l_expected_delivery_date=row['expected_delivery_date'] 
            l_total_cost=row['total_cost'] 
            l_orders_insert_str="INSERT INTO supply_chain.orders(order_id,supplier_id,order_date,expected_delivery_date,total_cost) VALUES('{0}','{1}','{2}','{3}','{4}')".format(l_order_id,l_supplier_id,l_order_date,l_expected_delivery_date,l_total_cost)
            # print(l_suppliers_insert_str)
            cursor.execute(l_orders_insert_str)

    conn.commit()
    cursor.close()
    conn.close() 
  
load_orders_data_csv()

