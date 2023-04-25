import csv
import random
import datetime 
import faker

fake=faker
# Define the field names for the CSV file
fieldnames = ['transaction_id', 'customer_id', 'deposit_amount', 'withdrawal_amount', 'transfer_amount','transaction_date']

def random_datetime(p_startyear=None):
    l_startyear=1980
    if p_startyear:
        l_startyear=p_startyear
    x =  datetime.datetime.strptime(str(l_startyear)+"-01-01", "%Y-%m-%d") + datetime.timedelta(
        seconds=random.randint(0, int((datetime.datetime.now() - datetime.datetime.strptime(str(l_startyear)+"-01-01", "%Y-%m-%d")).total_seconds()))
    )

    return x.strftime("%d/%m/%Y %H:%M:%S")
                                      
#print(random_datetime())

# Generate 10000 random records
records = []
for i in range(10000):
    transaction_id= random.randint(1000, 1000000)
    customer_id = i + 1
    deposit_amount=random.randint(1000, 10000)
    withdrawal_amount=random.randint(1000, 10000)
    transfer_amount=random.randint(1000, 10000)
    transaction_date=random_datetime()

    records.append({
        'transaction_id': transaction_id,
        'customer_id': customer_id,
        'deposit_amount': deposit_amount,
        'withdrawal_amount': withdrawal_amount,
        'transfer_amount': transfer_amount,
        'transaction_date': transaction_date,
    })

# Write the records to a CSV file
with open('transaction_data.csv', 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for record in records:
        writer.writerow(record)
