import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.svm import SVR
from sklearn.neural_network import MLPRegressor
import mlflow
import mlflow.sklearn

# Load data
df = pd.read_csv('output.csv')
df.ffill(inplace=True)

# Split data into features and target
X = df.drop(columns=['timestamp', '4. close'])  # Drop timestamp and close price (target)
y = df['4. close']  # Close price as the target variable

# Split data into train, validation, and test sets
X_train, X_temp, y_train, y_temp = train_test_split(X, y, test_size=0.3, random_state=42)
X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.5, random_state=42)

# Set the MLflow tracking URI to your server address
mlflow.set_tracking_uri("http://localhost:5000")  # Update this with your MLflow server address

# Initialize MLflow
mlflow.set_experiment('model_selection')

# Initialize models
models = {
    'DecisionTree': DecisionTreeRegressor(),
    'RandomForest': RandomForestRegressor(),
    'GradientBoosting': GradientBoostingRegressor(),
    'SVR': SVR(),
    'MLP': MLPRegressor()
}

best_model_name = None
best_model_score = float('-inf')

# Loop through models
for name, model in models.items():
    with mlflow.start_run(run_name=name):
        # Train the model on training data
        model.fit(X_train, y_train)
        
        # Evaluate the model on validation data
        score = model.score(X_val, y_val)
        
        # Print validation score
        print(f'{name} Validation Score: {score}')
        
        # Log parameters
        mlflow.log_param('model_name', name)
        
        # Log metrics
        mlflow.log_metric('validation_score', score)
        
        # Log model
        mlflow.sklearn.log_model(model, f'{name}_model')
        
        # Check if this model is the best so far
        if score > best_model_score:
            best_model_name = name
            best_model_score = score

# Print the best model name and its validation score
print(f'Best Model: {best_model_name}, Validation Score: {best_model_score}')
