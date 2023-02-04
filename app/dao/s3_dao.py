import config
import logging

import app.core.s3_core as s3_core

def get_image_data_from_path(path='folder_1/folder_2/image.jpg'):
    """Get image data from s3 path

    Args:
        path (str, optional): Path to image file in s3 bucket. Defaults to 'folder_1/folder_2/image.jpg'.

    Returns:
        bytes: Image data in readable buffer format - bytes
    """
    s3_client = s3_core.get_client()
    response = s3_client.get_object(Bucket=config.S3_BUCKET_NAME, Key=path)
    data = response['Body'].read()
    return data
