import csv
import random


headers = ['shipment_item_id', 'shipment_id', 'product_name', 'quantity_received','unit_price']

shipment_ids = list(range(1, 10001))
product_names = ['Product A', 'Product B', 'Product C', 'Product D', 'Product E']


with open('shipment_items.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(headers)


    for i in range(1, 10001):
        shipment_item_id = i
        shipment_id = random.choice(shipment_ids)
        product_name = random.choice(product_names)
        quantity_received = random.randint(1, 10)
        unit_price = round(random.uniform(1, 50), 2)


        writer.writerow([shipment_item_id, shipment_id, product_name, quantity_received, unit_price])
