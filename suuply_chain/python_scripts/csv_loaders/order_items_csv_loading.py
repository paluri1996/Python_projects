import psycopg2
import csv

def load_order_items_data_csv():
    conn = psycopg2.connect(
            host="127.0.0.1",
            database="tinitiate",
            user="tinitiate",
            password="tinitiate")

    cursor= conn.cursor()
    path = "C:\\Users\\rakes\\Python_practice\\suuply_chain\\data"

    with open(path+'\\order_items.csv', 'r') as csv_file:
        data = csv.DictReader(csv_file)
        # print(data) 

        # order_item_id,order_id,product_name,quantity,unit_price

        for row in data:
            # print(row)
            l_order_item_id=row["order_item_id"]
            l_order_id = row["order_id"]
            l_product_name=row['product_name']  
            l_quantity=row['quantity'] 
            l_unit_price=row['unit_price'] 
            l_order_items_insert_str="INSERT INTO supply_chain.order_items(order_item_id,order_id,product_name,quantity,unit_price) VALUES('{0}','{1}','{2}','{3}','{4}')".format(l_order_item_id,l_order_id,l_product_name,l_quantity,l_unit_price)
            # print(l_suppliers_insert_str)
            cursor.execute(l_order_items_insert_str)

    conn.commit()
    cursor.close()
    conn.close() 
  
load_order_items_data_csv()
