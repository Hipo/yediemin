# Yediemin

A package for bulletproof attachment serving in Django, Django Rest Framework.

## Getting Started

### Requirements
- Nginx
- Django Rest Framework
- Session Authentication.
- Django Storages



### Installation Steps

1) Install package.

> pip install yediemin

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

4) Use `YedieminFileField` in serializer for `FileField`.

```python
from yediemin import YedieminView

urlpatterns = [
    re_path(r'^yediemin/(?P<file_name>\S+)/$', YedieminView.as_view(), name='yediemin'),
]
```