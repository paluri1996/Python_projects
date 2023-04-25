import psycopg2
import csv

def load_risk_data_csv():
    conn = psycopg2.connect(
            host="127.0.0.1",
            database="tinitiate",
            user="tinitiate",
            password="tinitiate")

    cursor= conn.cursor()
    path = "C:\\Users\\rakes\\Python_practice\\calc_engine\\data\\risk_data"

    with open(path+'\\risk_data.csv', 'r') as csv_file:
        data = csv.DictReader(csv_file)
        # print(data) 

        for row in data:
            # print(row)
            l_risk_data_id = row["risk_data_id"]
            l_customer_id = row["customer_id"]
            l_product_id = row["product_id"]
            l_credit_score = row['credit_score']  
            l_default_probability = row['default_probability'] 
            l_market_value = row['market_value'] 
            l_volatility = row['volatility']
            l_operational_loss = row['operational_loss']
            l_risk_insert_str = "INSERT INTO calc_engine.customer(risk_data_id,customer_id,product_id,credit_score,default_probability,market_value,volatility,operational_loss) VALUES('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}')".format(l_risk_data_id,l_customer_id, l_product_id,l_credit_score,l_default_probability,l_market_value,l_volatility,l_operational_loss)
            print(l_risk_insert_str)
            cursor.execute(l_risk_insert_str)

    conn.commit()
    cursor.close()
    conn.close() 
  
load_risk_data_csv()