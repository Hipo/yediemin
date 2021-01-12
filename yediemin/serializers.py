from urllib.parse import urlencode

from django.urls import reverse
from django.core import signing

from rest_framework.fields import FileField


class YedieminFieldMixin:

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
