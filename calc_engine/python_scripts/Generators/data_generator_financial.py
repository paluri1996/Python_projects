import csv
import random
import faker
import datetime

fake=faker
# Define the field names for the CSV file
fieldnames = ['financial_data_id', 'company_id', 'statement_type', 'period_start', 'period_end', 'total_assets', 'total_liabilities', 'total_equity', 'net_income', 'operating_cash_flow', 'investing_cash_flow', 'financing_cash_flow']
statement_types = ['comprehensive income', 'changes in equity', 'retained earnings', 'interim', 'segmental', 'budgeted', 'regulatory', 'compliance']
total_asset = ['physical assets', 'financial assets', 'intangible assets', 'fixed assets', 'non-current assets', 'current assets', 'assets under management']

def random_datetime(p_startyear=None):
    l_startyear=1980
    if p_startyear:
        l_startyear=p_startyear
    return datetime.datetime.strptime(str(l_startyear)+"-01-01", "%Y-%m-%d") + datetime.timedelta(
        seconds=random.randint(0, int((datetime.datetime.now() - datetime.datetime.strptime(str(l_startyear)+"-01-01", "%Y-%m-%d")).total_seconds())),
    )

records = []

for i in range(10000):
    # Generate 10000 random records
    financial_data_id= i + 1
    company_id = random.randint(1, 10000)
    statement_type=random.choice(statement_types)
    period_start=repr(random_datetime)
    period_end = repr(random_datetime)
    total_assets=random.choice(total_asset)
    total_liabilities=random.randint(1, 2)
    total_equity = random.randint(1, 2)
    net_income=random.randint(1, 2)
    operating_cash_flow=random.randint(1, 2)
    investing_cash_flow=random.randint(1, 2)
    financing_cash_flow=random.randint(1, 2)

    records.append({
        'financial_data_id': financial_data_id,
        'company_id': company_id,
        'statement_type': statement_type,
        'period_start': period_start,
        'period_end': period_end,
        'total_assets': total_assets,
        'total_liabilities': total_liabilities,
        'total_equity': total_equity,
        'net_income': net_income,
        'operating_cash_flow': operating_cash_flow,
        'investing_cash_flow' : investing_cash_flow,
        'financing_cash_flow' : financing_cash_flow
    })

# Write the records to a CSV file
with open('financial_data.csv', 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for record in records:
        writer.writerow(record)
