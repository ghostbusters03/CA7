import numpy as np
import pandas as pd
import yfinance as yf
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

# Step 1: Fetch and Prepare the Data
def fetch_stock_data(ticker):
    stock_data = yf.download(ticker, start="2020-01-01", end="2023-01-01")
    stock_data = stock_data[['Close']]
    stock_data['Date'] = stock_data.index
    stock_data.reset_index(drop=True, inplace=True)
    return stock_data

# Fetch data
ticker = 'AAPL'  # Example ticker
stock_data = fetch_stock_data(ticker)

# Prepare the data
stock_data['Day'] = np.arange(len(stock_data))
X = stock_data[['Day']]
y = stock_data['Close']

# Step 2: Split the Data
X_train, X_temp, y_train, y_temp = train_test_split(X, y, test_size=0.3, random_state=42)
X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.5, random_state=42)

# Step 3: Train the Model
model = LinearRegression()
model.fit(X_train, y_train)

# Step 4: Validate the Model
y_val_pred = model.predict(X_val)
val_mse = mean_squared_error(y_val, y_val_pred)
val_r2 = r2_score(y_val, y_val_pred)
print(f"Validation MSE: {val_mse}")
print(f"Validation R²: {val_r2}")

# Step 5: Test the Model
y_test_pred = model.predict(X_test)
test_mse = mean_squared_error(y_test, y_test_pred)
test_r2 = r2_score(y_test, y_test_pred)
print(f"Test MSE: {test_mse}")
print(f"Test R²: {test_r2}")

# Plotting the results
plt.figure(figsize=(10, 5))
plt.scatter(X_train, y_train, color='blue', label='Training data')
plt.scatter(X_val, y_val, color='green', label='Validation data')
plt.scatter(X_test, y_test, color='red', label='Testing data')
plt.plot(X, model.predict(X), color='black', linewidth=2, label='Model prediction')
plt.xlabel('Day')
plt.ylabel('Close Price')
plt.title('Stock Price Prediction')
plt.legend()
plt.show()
