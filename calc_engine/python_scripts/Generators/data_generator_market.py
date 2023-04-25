import csv
import json
import random
import datetime 
import time
import faker

fake=faker
# Define the field names for the CSV file
fieldnames = ['market_data_id', 'market_trend', 'economic_indicator', 'external_factor', 'value']
market_trends = ['Bullish', 'Bearish', 'Sideways']
economic_indicators = ['GDP', 'Unemployment Rate', 'Inflation Rate', 'Retail Sales',
                       'Housing Starts', 'Trade Balance', 'Consumer Price Index',
                       'Employment Rate', 'Industrial Production']
external_factors = ['Political Stability', 'Oil Prices', 'Interest Rates',
                    'Consumer Confidence', 'Exchange Rates', 'Stock Market']


# Generate 10000 random records
records = []
for i in range(10000):
    market_data_id= i + 1
    market_trend = random.choice(market_trends)
    economic_indicator=random.choice(economic_indicators)
    external_factor=random.choice(external_factors)
    value=random.randint(1000, 10000)

    records.append({
        'market_data_id': market_data_id,
        'market_trend': market_trend,
        'economic_indicator': economic_indicator,
        'external_factor': external_factor,
        'value': value
    })

# Write the records to a CSV file
with open('market_data.csv', 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for record in records:
        writer.writerow(record)
