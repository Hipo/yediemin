from urllib.parse import urlencode

from django.urls import reverse
from django.core import signing

from rest_framework.fields import FileField

from yediemin.storages import PrivateS3Boto3Storage


class YedieminFieldMixin:

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.storage = PrivateS3Boto3Storage

    def to_representation(self, value):
        file_url = super().to_representation(value)

        request = self.context["request"]

        key = signing.dumps({
            # Passing to url path.
            "file_name": value.name,

            # Redirection
            "file_url": file_url,

            # Authentication
            "user_id": request.user.id
        })

        yediemin_base_url = request.build_absolute_uri(reverse("yediemin", kwargs={"file_name": value.name}))
        query_string = urlencode({"key": key})
        url = f"{yediemin_base_url}?{query_string}"
        return url


class YedieminFileField(YedieminFieldMixin, FileField):
    pass
