from storages.backends.s3boto3 import S3Boto3Storage


class PrivateS3Boto3Storage(S3Boto3Storage):

    def get_default_settings(self):
        settings = super().get_default_settings()
        settings["default_acl"] = "private"
        return settings
