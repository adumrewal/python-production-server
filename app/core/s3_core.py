import boto3
import config
import logging

_S3_CLIENT = None


def initialize() -> None:
    global _S3_CLIENT
    _S3_CLIENT = boto3.client(
        's3',
        aws_access_key_id=config.S3_ACCESS_KEY_ID,
        aws_secret_access_key=config.S3_SECRET_ACCESS_KEY
    )
    if _S3_CLIENT is not None:
        logging.info({'message': 'S3 client initialized successfully'})


def get_client():
    global _S3_CLIENT
    if _S3_CLIENT is None:
        logging.info({'message': 'S3 client requested without initialization'})
        initialize()
    return _S3_CLIENT
