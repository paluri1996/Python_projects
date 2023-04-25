import psycopg2
import os
import csv


def load_market_data_csv():
    conn = psycopg2.connect(
            host="127.0.0.1",
            database="tinitiate",
            user="tinitiate",
            password="tinitiate")

    cursor= conn.cursor()
    path = "C:\\Users\\rakes\\Python_practice\\calc_engine\\data\\market_data"

    with open(path+'\\market_data.csv', 'r') as csv_file:
        data = csv.DictReader(csv_file)
        # print(data) 

        for row in data:
            # print(row)
            l_market_data_id=row["market_data_id"]
            l_market_trend = row["market_trend"]
            l_economic_indicator=row['economic_indicator']  
            l_external_factor=row['external_factor'] 
            l_value=row['value'] 
            l_market_insert_str="INSERT INTO calc_engine.market_data(market_data_id,market_trend,economic_indicator,external_factor,value) VALUES('{0}','{1}','{2}','{3}','{4}')".format(l_market_data_id, l_market_trend,l_economic_indicator,l_external_factor,l_value)
            print(l_market_insert_str)
            cursor.execute(l_market_insert_str)

    
    conn.commit()
    cursor.close()
    conn.close() 
  
load_market_data_csv()

