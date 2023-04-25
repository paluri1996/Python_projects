#importing json file
import json
#importing postgress connection
import psycopg2
from datetime import datetime
import os
import csv

def load_products_csv():
    #connection
    conn = psycopg2.connect(
            host="127.0.0.1",
            database="tinitiate",
            user="tinitiate",
            password="tinitiate")

    cursor= conn.cursor()

    # The path where the JSON files are stored
    path = "C:\\Users\\rakes\\Downloads\\batch_1_bills\\batch_1_bills"
    # Loop through all files in the directory

    with open('products.csv', 'r') as csv_file:
        data = csv.reader(csv_file)
        # print(data) 

    with open('products.csv', newline='', mode='r', encoding='utf-8-sig') as csvfile:
        reader = csv.DictReader(csvfile)
        
        for row in reader:
            print(row)
            # {'product_id': '1', 'product_category': 'FROZEN', 'product_name': 'Ice Cream', 'unit_price': '2.5'}
            # data = csv.load      
            l_product_id =row["product_id"]
            l_product_category = row["product_category"]
            l_product_name=row['product_name']  
            l_unit_price=row['unit_price'] 
            l_products_insert_str="INSERT INTO data_loading.products(product_id, product_category,product_name,product_price) VALUES({0},'{1}','{2}',{3})".format(l_product_id, l_product_category,l_product_name,l_unit_price)
            print(l_products_insert_str)
            cursor.execute(l_products_insert_str)

    cursor.close()
    conn.commit()
    conn.close()


def load_bills_json():
       #connection
    conn = psycopg2.connect(
            host="127.0.0.1",
            database="tinitiate",
            user="tinitiate",
            password="tinitiate")

    cursor= conn.cursor()

    # The path where the JSON files are stored
    path = "C:\\Users\\rakes\\Downloads\\batch_1_bills\\batch_1_bills"
    # Loop through all files in the directory

    for filename in os.listdir(path):
        if filename.endswith(".json"):
            inputfile = os.path.join(path, filename)
            print(inputfile)
            with open(inputfile,'r') as f:    
                data = json.load(f)
                # print(data)
                BILLId = data["BillID"]
                BillDate = data["BillDate"]
                StoreID=data['StoreID']  
                BillDate=data['BillDate'] 
                datetime_obj = datetime.strptime(BillDate, '%m/%d/%Y %H:%M:%S')

                query="INSERT INTO data_loading.bills (bill_id, bill_date, store_id) VALUES({},'{}',{})".format(BILLId,datetime_obj,StoreID)
                try:
                    cursor.execute(query)
                except Exception as e:
                    print(type(e).__name__, e)
                    print(BILLId,datetime_obj,StoreID)
                    
                # conn.commit()
    # cursor.close()
    # conn.close()


    for filename in os.listdir(path):
        if filename.endswith(".json"):
            inputfile = os.path.join(path, filename)
            print(inputfile)
            with open(inputfile,'r') as f:    
                data = json.load(f)
                print(data)
                print (data['BillDetails'])
                l_seq=1
                for bill_detail in data['BillDetails']:
                    l_bill_id=data['BillID']
                    l_bill_detail_id=str(l_bill_id )+ '_'+str(l_seq)
                    l_seq=l_seq+1
                    l_quantity= bill_detail['Quantity']
                    l_product_id=bill_detail['ProductID']
                    l_bill_details_insert_str="INSERT INTO data_loading.bill_details(bill_detail_id, bill_id,quantity,product_id) VALUES('{0}',{1},{2},{3});".format(l_bill_detail_id,l_bill_id,l_quantity,l_product_id)
                    # l_bill_details_insert_str="INSERT INTO data_loading.bill_details(bill_detail_id, bill_id,quantity,product_id) VALUES({0},{1},{2},{3})"
                    print(l_bill_details_insert_str)
                    
                    try:
                        cursor.execute(l_bill_details_insert_str)
                    except Exception as e:
                        print(type(e).__name__, e)
                        print(l_bill_detail_id,l_bill_id,l_quantity,l_product_id)
    conn.commit()
    cursor.close()
    conn.close() 

load_bills_json()           
                
   



    
  
   


"""
for filename in os.listdir(path):
    if filename.endswith(".json"):
        inputfile = os.path.join(path, filename)
        print(inputfile)
        with open(inputfile,'r') as f:    
            data = json.load(f)
            # print(data)
            BILLId = data["BillID"]
            BillDate = data["BillDate"]
            StoreID=data['StoreID']  
            BillDate=data['BillDate'] 
            datetime_obj = datetime.strptime(BillDate, '%m/%d/%Y %H:%M:%S')

            query="INSERT INTO data_loading.bills (bill_id, bill_date, store_id) VALUES({},'{}',{})".format(BILLId,datetime_obj,StoreID)
            cursor.execute(query)
            conn.commit()
cursor.close()
conn.close()

l_insert_bill_str='' 

for bill in data['BillDetails']:
    insert_bill_detail_str=""
    Product=bill['ProductID']
    Quantity=bill['Quantity']
    # print(Product,Quantity)



#     bill_detail_id 		int
# ,bill_id			int
# ,quantity           decimal
# ,product_id	

# l_bill_details_insert_str="INSERT INTO data_loading.bill_details(bill_detail_id, bill_id,quantity,product_id) VALUES({0},{1},{2},{3})"
l_bill_detail_id = ""

for filename in os.listdir(path):
    if filename.endswith(".json"):
        inputfile = os.path.join(path, filename)
        print(inputfile)
        with open(inputfile,'r') as f:    
            data = json.load(f)
            print(data)
            print (data['BillDetails'])
            l_seq=1
            for bill_detail in data['BillDetails']:
                l_bill_id=data['BillID']
                l_bill_detail_id=str(l_bill_id )+ '_'+str(l_seq)
                l_seq=l_seq+1
                l_quantity= bill_detail['Quantity']
                l_product_id=bill_detail['ProductID']
                l_bill_details_insert_str="INSERT INTO data_loading.bill_details(bill_detail_id, bill_id,quantity,product_id) VALUES({0},{1},{2},{3});".format(l_bill_detail_id,l_bill_id,l_quantity,l_product_id)
                # l_bill_details_insert_str="INSERT INTO data_loading.bill_details(bill_detail_id, bill_id,quantity,product_id) VALUES({0},{1},{2},{3})"
                print(l_bill_details_insert_str)
                
                
                
    break        
"""               
    
"""        
            # l_BillDetails = data["BillDetails"]
            l_bill_detail_id = data["bill_id"]+str(l_seq)
            l_bill_id=data['bill_id']
            l_quantity = ['quantity']  
            product_id=data['product_id'] 
            # datetime_obj = datetime.strptime(BillDate, '%m/%d/%Y %H:%M:%S')

            query=l_bill_details_insert_str.format(bill_detail_id, bill_id,product_id)
            cursor.execute(query)
            conn.commit()
cursor.close()
conn.close()

l_insert_bill_str='' 

# for bill_details in data['BillDetails']:
#     insert_bill_detail_str=""
#     Product=bill_details['ProductID']
#     Quantity=bill_details['Quantity']
#     print(Product,Quantity)
"""

