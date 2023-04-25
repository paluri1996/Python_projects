import psycopg2
import csv

def load_shipment_items_csv():
    conn = psycopg2.connect(
            host="127.0.0.1",
            database="tinitiate",
            user="tinitiate",
            password="tinitiate")

    cursor= conn.cursor()
    path = "C:\\Users\\rakes\\Python_practice\\suuply_chain\\data"

    with open(path+'\\shipment_items.csv', 'r') as csv_file:
        data = csv.DictReader(csv_file)
        # print(data) 

        # shipment_item_id,shipment_id,product_name,quantity_received,unit_price

        for row in data:
            # print(row)
            l_shipment_item_id = row["shipment_item_id"]
            l_shipment_id=row["shipment_id"]
            l_product_name=row['product_name']  
            l_quantity_received=row['quantity_received'] 
            l_unit_price=row['unit_price'] 
            l_shipment_items_insert_str="INSERT INTO supply_chain.shipment_items(shipment_item_id,shipment_id,product_name,quantity_received,unit_price) VALUES('{0}','{1}','{2}','{3}','{4}')".format( l_shipment_item_id,l_shipment_id,l_product_name,l_quantity_received,l_unit_price)
            # print(l_suppliers_insert_str)
            cursor.execute(l_shipment_items_insert_str)

    conn.commit()
    cursor.close()
    conn.close() 
  
load_shipment_items_csv()