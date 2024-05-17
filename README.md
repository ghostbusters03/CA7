TASK 1: i200822  
Used Stock Data taken at 1 minute intervals and stored in a directory data_store when the script is running continuously  
Used Google Cloud to create a bucket: mlopsca7  
DVC is used for data version control  

TASK 3: i200503  
- Cloned the repository  
- Used dvc pull  
- Copied the pulled JSON file to data folder (following Sir Hammad's repository)  
- Made changes accordingly to all the files train.py, conda.yaml, MLproject, python_env.yaml  
- mlflow run . --env-manager local  
- mlflow server  
- Did the optional task aswell by doing hyperparameter tuning: Results are as follows:

![graph](https://github.com/ghostbusters03/CA7/assets/125590201/b40a09cc-b2c7-4712-8a3a-0a2bfe068593)



1) --alpha 0.5 --l1_ratio 0.1
     
Validation MSE: 287.3260985442783

Validation R²: 0.7397263246993735

Test MSE: 285.6632065819075

Test R²: 0.698707339893039

2) --alpha 0.3 --l1_ratio 0.2
Validation MSE: 287.3260985442783

Validation R²: 0.7397263246993735

Test MSE: 285.6632065819075

Test R²: 0.698707339893039
