import boto3
import logging
import config.config as cfg
from botocore.exceptions import ClientError

logger = logging.getLogger(cfg.logger_app_name)


class AwsHelper:
    def __init__(self):
        self.s3_client = boto3.client('s3', region_name=cfg.AWS_REGION)

    def download_from_s3(self, bucket_name: str, key_name: str, localpath: str):
        logger.info('Ha comenzado la descarga del objeto ... \n')
        try:
            self.s3_client.download_file(bucket_name, key_name, localpath)
            logger.info('Se ha descargado el objeto correctamente.')
        except (Exception, ClientError) as e:
            logger.error(f'Error descargando desde S3, {e}')
            if e.response['Error']['Code'] == '404':
                logging.info('El objeto no existe')
        return None

    def upload_to_s3(self, localpath: str, bucket_name: str, key_name: str):
        logger.info('Se ha empezado a cargar el objeto a S3 ... \n')
        try:
            self.s3_client.upload_file(localpath, bucket_name, key_name)
            logger.info('Se ha cargado el objeto en S3 correctamente.')
        except (Exception, ClientError) as e:
            logging.error(f'Error cargando a S3, {e}')
        return None
