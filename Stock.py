import requests
import json
import schedule
import time
from datetime import datetime
import os

def fetch_and_save_data():
    # API URL
    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=1min&apikey=UHVHCBK2ZN33B2S3'

    # Sending GET request to the API
    response = requests.get(url)

    # Parsing the JSON response
    data = response.json()

    # Ensure the directory exists
    directory = 'data_store'  # Specify your path
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Format the current timestamp and use it as the file name
    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    file_path = f"{directory}/stock_data.json"

    # Writing data to the file
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

    print(f"Data saved to {file_path}")

# Schedule to run every 30 minutes
schedule.every(1).minutes.do(fetch_and_save_data)

# Keep the script running
while True:
    schedule.run_pending()
    time.sleep(1)
