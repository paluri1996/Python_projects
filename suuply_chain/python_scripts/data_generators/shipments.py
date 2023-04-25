import csv
import random
import string
import pandas as pd


headers = ['shipment_id', 'order_id', 'shipment_date','carrier_name', 'tracking_number']


order_ids = list(range(1, 10001))
carrier_names = ['UPS', 'FedEx', 'DHL', 'USPS']
shipment_dates = pd.date_range(start='2020-01-01', end='2022-12-31', freq='D')


with open('shipments.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(headers)


    for i in range(1, 10001):
        shipment_id = i
        order_id = random.choice(order_ids)
        shipment_date = random.choice(shipment_dates).strftime('%Y-%m-%d')
        carrier_name = random.choice(carrier_names)
        tracking_number = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))


        writer.writerow([shipment_id, order_id, shipment_date,  carrier_name, tracking_number])
