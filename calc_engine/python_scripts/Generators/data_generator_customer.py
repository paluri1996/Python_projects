import csv
import random

# Define the field names for the CSV file
fieldnames = ['customer_id', 'customer_name', 'account_number', 'account_type', 'account_balance']
first_names = ['Emma', 'Olivia', 'Ava', 'Isabella', 'Sophia', 'Mia', 'Charlotte', 'Amelia', 'Harper', 'Evelyn']
last_names = ['Smith', 'Johnson', 'Brown', 'Taylor', 'Miller', 'Anderson', 'Wilson', 'Davis', 'Garcia', 'Martinez']


# Generate 10000 random records
records = []
for i in range(10000):
    customer_id = i + 1
    # customer_name = f"Customer {customer_id}"
    first_name = random.choice(first_names)
    last_name = random.choice(last_names)
    customer_name = f"{first_name} {last_name}"
    account_number = random.randint(1000, 100000)
    account_type = random.choice(['savings', 'checking', 'credit'])
    account_balance = random.randint(1000, 100000)
    records.append({
        'customer_id': customer_id,
        'customer_name': customer_name,
        'account_number': account_number,
        'account_type': account_type,
        'account_balance': account_balance
    })

# Write the records to a CSV file
with open('customer_data.csv', 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for record in records:
        writer.writerow(record)