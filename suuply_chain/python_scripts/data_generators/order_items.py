import csv
import random


header = ['order_item_id', 'order_id', 'product_name', 'quantity', 'unit_price']


rows = []
for i in range(10000):
    order_item_id = i + 1
    order_id = random.randint(1, 1000)
    product_name = f'Product {random.randint(1, 100)}'
    quantity = random.randint(1, 10)
    unit_price = round(random.uniform(10.0, 100.0), 2)
    rows.append([order_item_id, order_id, product_name, quantity, unit_price])


with open('order_items.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(rows)
