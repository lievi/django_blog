from storages.backends.s3boto3 import S3Boto3Storage


class MediaStorage(S3Boto3Storage):
    """Configuring the S3 with the location and telling to not overwrite"""
    location = 'media'
    file_overwrite = False