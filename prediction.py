import logging
import config.config as cfg
from aws.aws_helper import AwsHelper
from utilities.utils import load_model, prediction
from utilities.data_wrangling import load_data, export_data

aws = AwsHelper()

logger = logging.getLogger(cfg.logger_app_name)


def main():
    logger.info('El proceso de prediccion ha comenzado ... \n')
    aws.download_from_s3(bucket_name=cfg.S3_BUCKET,
                         key_name=f'{cfg.S3_KEY}/input/input_churn_data.csv',
                         localpath='data/input_churn_data.csv')
    data = load_data(filepath='data/input_churn_data.csv')
    model = load_model(filepath='models/dtree.joblib')
    data = prediction(data=data, model=model)
    export_data(df=data, filepath='data/results.csv')
    aws.upload_to_s3(localpath='data/results.csv',
                     bucket_name=cfg.S3_BUCKET, key_name=f'{cfg.S3_KEY}/results/results.csv')
    return True


if __name__ == '__main__':
    main()
