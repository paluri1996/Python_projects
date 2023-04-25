import psycopg2
import csv

def load_shipments_data_csv():
    conn = psycopg2.connect(
            host="127.0.0.1",
            database="tinitiate",
            user="tinitiate",
            password="tinitiate")

    cursor= conn.cursor()
    path = "C:\\Users\\rakes\\Python_practice\\suuply_chain\\data"

    with open(path+'\\shipments.csv', 'r') as csv_file:
        data = csv.DictReader(csv_file)
        # print(data) 

        # shipment_id,order_id,shipment_date,carrier_name,tracking_number

        for row in data:
            # print(row)
            l_shipment_id=row["shipment_id"]
            l_order_id = row["order_id"]
            l_shipment_date=row['shipment_date']  
            l_carrier_name=row['carrier_name'] 
            l_tracking_number=row['tracking_number'] 
            l_shipments_insert_str="INSERT INTO supply_chain.shipments(shipment_id,order_id,shipment_date,carrier_name,tracking_number) VALUES('{0}','{1}','{2}','{3}','{4}')".format(l_shipment_id,l_order_id,l_shipment_date,l_carrier_name,l_tracking_number)
            # print(l_suppliers_insert_str)
            cursor.execute(l_shipments_insert_str)

    conn.commit()
    cursor.close()
    conn.close() 
  
load_shipments_data_csv()
