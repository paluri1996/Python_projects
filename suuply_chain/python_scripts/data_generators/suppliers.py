import csv
import random


headers = ['supplier_id', 'name', 'email', 'phone_number', 'address', 'city', 'state', 'zip_code']
name_list = ['ABC Suppliers', 'XYZ Corporation', 'Acme Inc.', 'Global Trading Co.', 'Smith & Sons']
domain_list = ['gmail.com', 'yahoo.com', 'hotmail.com', 'outlook.com']
state_list = ['California', 'New York', 'Texas', 'Florida', 'Illinois', 'Pennsylvania', 'Ohio']
zip_code_list = ['10001', '90210', '75001', '33101', '60601']


with open('suppliers.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(headers)

    for i in range(1, 10001):
        supplier_id = i
        name = random.choice(name_list)
        username = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz0123456789', k=8))
        domain = random.choice(domain_list)
        email = username + '@' + domain
        phone_number = ''.join(random.choices('0123456789', k=10))
        address = str(random.randint(1, 9999)) + ' ' + ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=10)) + ' St.'
        city = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=10))
        state = random.choice(state_list)
        zip_code = random.choice(zip_code_list)

        writer.writerow([supplier_id, name, email, phone_number, address, city, state, zip_code])
