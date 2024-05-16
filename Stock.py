import requests
import json

# API URL
url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=UHVHCBK2ZN33B2S3'

# Sending GET request to the API
response = requests.get(url)

# Parsing the JSON response
data = response.json()

# File to save the data
file_path = 'stock_data.json'

# Writing data to the file
with open(file_path, 'w') as file:
    json.dump(data, file, indent=4)

print(f"Data saved to {file_path}")
