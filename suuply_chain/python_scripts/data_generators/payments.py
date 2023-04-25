import csv
import random
from datetime import datetime, timedelta


headers = ['payment_id', 'supplier_id', 'payment_date', 'payment_method', 'amount']


supplier_ids = list(range(1, 10001))
payment_methods = ['Credit Card', 'Debit Card', 'PayPal', 'Bank Transfer']


with open('payments.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(headers)


    for i in range(1, 10001):
        payment_id = i
        supplier_id = random.choice(supplier_ids)
        payment_date = datetime.today() - timedelta(days=random.randint(1, 365))
        payment_method = random.choice(payment_methods)
        amount = round(random.uniform(10.0, 1000.0), 2)


        writer.writerow([payment_id, supplier_id, payment_date.strftime('%Y-%m-%d'), payment_method, amount])
