from storages.backends.s3boto3 import S3Boto3Storage

"""
This file required by S3Boto3Storage to configure user uploads to AWS S3 bucket
"""


class MediaStorage(S3Boto3Storage):
    location = 'media'
    file_overwrite = False
