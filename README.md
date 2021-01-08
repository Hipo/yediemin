# Yediemin

A package for bulletproof attachment serving in Django Rest Framework.

## Getting Started

### Requirements
- Nginx
- Django Rest Framework
- Session Authentication
- Django Storages (S3)

### Installation Steps

1) Install package from [PyPi](https://pypi.org/project/yediemin/).

```sh
pip install yediemin
```

2) Add the view to `urls.py`

```python
from yediemin import YedieminView

urlpatterns = [
    re_path(r'^yediemin/(?P<file_name>\S+)/$', YedieminView.as_view(), name='yediemin'),
]
```

3) Configure Nginx. Place the configuration below under your server.

```
location /yediemin-files/ {
            internal;
            resolver 8.8.8.8;
            set $redirect_uri "$upstream_http_redirect_uri";

            proxy_buffering off;
            proxy_pass $redirect_uri;
}
```

4) Use ``YedieminFileField`` in serializer for `FileField`.

```python
from yediemin import YedieminFileField

class AttachmentSerializer(serializers.ModelSerializer):
    file = YedieminFileField()

    class Meta:
        model = Attachment
        fields = (
            "id",
            "file",
        )
```

5) Upload files to S3 with `YedieminFileField`. Yediemin requires [presigned object url](https://docs.aws.amazon.com/AmazonS3/latest/dev/ShareObjectPreSignedURL.html).

### Settings

- `YEDIEMIN_HIDDEN_REDIRECT_PATH`

Default: `yediemin-files`.
It should be same with location in nginx configuration.

- `YEDIEMIN_AUTHENTICATION_CLASS`

Default: `rest_framework.authentication.SessionAuthentication`

- `YEDIEMIN_EXPIRE_IN`

Default: `2592000` seconds which is 1 month.