import os
from dotenv import load_dotenv

load_dotenv(override=False)


class Config:
    APP_NAME = os.getenv('APP_NAME', 'ZS3')

    # Environment
    ENVIRONMENT = os.getenv('ENVIRONMENT', 'PRODUCTION')
    REGION = os.getenv('REGION', 'IND')
    LANGUAGE = os.getenv('APP_LANGUAGE', 'EN')

    # Log
    LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')

    # AWS
    AWS = {
        's3_bucket_name': os.environ['AWS_S3_BUCKET_NAME'],
        's3_upload_bucket_name': os.environ['AWS_S3_UPLOAD_BUCKET_NAME'],
        's3_key_id': os.environ['AWS_S3_KEY_ID'],
        's3_key_secret': os.environ['AWS_S3_SECRET_KEY'],
        'region': os.environ['AWS_S3_REGION']
    }
