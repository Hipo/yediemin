# yediemin

![](https://i.imgur.com/V7NKAqH.jpg)

## getting started

requirements
- django rest framework
- nginx
- session authentication.

steps
- install package.

> pip install yediemin

- add the view `urls.py`

```python
from yediemin import YedieminView

urlpatterns = [
    path(r'yediemin/', YedieminView.as_view(), name='yediemin'),
]
```

- configure nginx. place the configuration below under your server.

```
location /yediemin-files/ {
            internal;
            resolver 8.8.8.8;
            set $redirect_uri "$upstream_http_redirect_uri";

            proxy_buffering off;
            proxy_pass $redirect_uri;
}
```

- use `YedieminField` in serializer for `FileField`.
