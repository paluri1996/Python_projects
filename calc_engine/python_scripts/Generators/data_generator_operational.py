import csv
import json
import random
import datetime 
import faker

fake=faker
# Define the field names for the CSV file
fieldnames = ['operational_id', 'customer_id', 'supplier_id', 'transaction_date', 'transaction_type','quantity','price']
transaction_types = ['Sale', 'Purchase', 'Return', 'Adjustment', 'Transfer', 'Disposal', 'Credit', 'Debit']

def random_datetime(p_startyear=None):
    l_startyear=1980
    if p_startyear:
        l_startyear=p_startyear
    return datetime.datetime.strptime(str(l_startyear)+"-01-01", "%Y-%m-%d") + datetime.timedelta(
        seconds=random.randint(0, int((datetime.datetime.now() - datetime.datetime.strptime(str(l_startyear)+"-01-01", "%Y-%m-%d")).total_seconds())),
    )

# Generate 10000 random records
records = []
for i in range(10000):
    operational_id= random.randint(1000, 1000000)
    customer_id = i + 1
    supplier_id=random.randint(1000, 10000)
    transaction_date=repr(random_datetime)
    transaction_type=random.choice(transaction_types)
    quantity=random.randint(1, 20)
    price=random.randint(1000, 10000)


    records.append({
        'operational_id': operational_id,
        'customer_id': customer_id,
        'supplier_id': supplier_id,
        'transaction_date': transaction_date,
        'transaction_type': transaction_type,
        'quantity': quantity,
        'price': price
    })

# Write the records to a CSV file
with open('operational_data.csv', 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for record in records:
        writer.writerow(record)
