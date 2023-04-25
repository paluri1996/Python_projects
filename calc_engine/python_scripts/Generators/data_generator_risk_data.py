import csv
import random
import faker

fake=faker
# Define the field names for the CSV file
fieldnames = ['risk_data_id', 'customer_id', 'product_id', 'credit_score', 'default_probability', 'market_value', 'volatility', 'operational_loss']

# Generate 10000 random records
records = []
for i in range(10000):
    risk_data_id = i + 1
    customer_id = i + 1
    product_id = i + 1
    credit_score = random.randint(0, 1)
    default_probability = random.randint(0, 1)
    market_value = random.randint(0, 1)
    volatility = random.randint(0, 1)
    operational_loss = random.randint(0, 1)

    records.append({
        'risk_data_id': risk_data_id,
        'customer_id': customer_id,
        'product_id': product_id,
        'credit_score': credit_score,
        'default_probability': default_probability,
        'market_value': market_value,
        'volatility': volatility,
        'operational_loss': operational_loss
    })

# Write the records to a CSV file
with open('risk_data.csv', 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for record in records:
        writer.writerow(record)
