import csv
import random
from datetime import datetime, timedelta


headers = ['order_id', 'supplier_id', 'order_date', 'expected_delivery_date', 'total_cost']


supplier_ids = list(range(1, 10001))


with open('orders.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(headers)

    for i in range(1, 10001):
        order_id = i
        supplier_id = random.choice(supplier_ids)
        order_date = datetime.today() - timedelta(days=random.randint(1, 365))
        expected_delivery_date = order_date + timedelta(days=random.randint(1, 30))
        total_cost = round(random.uniform(100.0, 10000.0), 2)


        writer.writerow([order_id, supplier_id, order_date.strftime('%Y-%m-%d'), expected_delivery_date.strftime('%Y-%m-%d'), total_cost])

