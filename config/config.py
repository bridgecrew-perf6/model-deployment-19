import sys
import logging

# Logger configuration -----------------------------------------------------------------------------------------------

logger_app_name = 'model-deployment'
logger = logging.getLogger(logger_app_name)
logger.setLevel(logging.INFO)
consoleHandle = logging.StreamHandler(sys.stdout)
consoleHandle.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
consoleHandle.setFormatter(formatter)
logger.addHandler(consoleHandle)

# AWS ----------------------------------------------------------------------------------------------------------------

AWS_REGION = 'us-east-1'

# S3

S3_BUCKET = 'banking-data'
S3_KEY = 'churn-modeling'

# Project ------------------------------------------------------------------------------------------------------------

SEED = 42

NUMERICAL_FEATURES = ['CreditScore', 'Age', 'Tenure', 'Balance',
                      'NumOfProducts', 'EstimatedSalary']

CATEGORICAL_FEATURES = ['Geography', 'Gender', 'HasCrCard', 'IsActiveMember']


