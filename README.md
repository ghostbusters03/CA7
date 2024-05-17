TASK 1:
Used Stock Data taken at 1 minute intervals and stored in a directory data_store when the script is running continiously
Used Google Cloud to create a bucket: mlopsca7
DVC is used for data version control



TASK 2:  (done by i200707)
Data is fetched and preprocessed.  

Following models are applied using MLflow:
  DecisionTreeRegressor
  RandomForestRegressor
  GradientBoostingRegressor
  SVR
  MLPRegressor

Relevant parameters and metrics are logged. Best model is selected based on validation score which turned out to be Decision Tree. Registered it using MLflow and containerized it. 

  
