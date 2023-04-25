import csv
import random
import faker

fake=faker
# Define the field names for the CSV file
fieldnames = ['compliance_data_id', 'customer_id', 'transaction_id', 'transaction_amount', 'transaction_date','aml_check_passed','kyc_check_passed']
aml_check_passed_state = ['yes', 'no']
kyc_check_passed_state = ['yes', 'no']
# Generate 10000 random records
records = []

for i in range(10000):
    compliance_data_id= i + 1
    customer_id = i + 1
    transaction_id=random.randint(1, 10000)
    transaction_amount=random.randint(1, 1000)
    transaction_date=random.randint(1000, 10000)
    aml_check_passed=random.choice(aml_check_passed_state)
    kyc_check_passed=random.choice(kyc_check_passed_state)

    records.append({
        'compliance_data_id': compliance_data_id,
        'customer_id': customer_id,
        'transaction_id': transaction_id,
        'transaction_amount': transaction_amount,
        'transaction_date': transaction_date,
        'aml_check_passed': aml_check_passed,
        'kyc_check_passed': kyc_check_passed
    })

# Write the records to a CSV file
with open('compliance_data.csv', 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for record in records:
        writer.writerow(record)
