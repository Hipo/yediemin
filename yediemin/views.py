from django.core.signing import BadSignature, SignatureExpired
from rest_framework.exceptions import PermissionDenied
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from django.core import signing

from yediemin.settings import AUTHENTICATION_CLASSES, HIDDEN_REDIRECT_PATH


class YedieminView(GenericAPIView):
    permission_classes = []
    authentication_classes = AUTHENTICATION_CLASSES

    def get(self, request, *args, **kwargs):
        try:
            key = request.query_params.get("key", "")
        except (BadSignature, SignatureExpired) as exc:
            raise PermissionDenied()

        values_in_key = signing.loads(key)

        try:
            file_name_in_key = values_in_key["file_name"]
            file_url_in_key = values_in_key["file_url"]
            user_id_in_key = values_in_key["user_id"]
        except AttributeError:
            raise PermissionDenied()

        if file_name_in_key != kwargs.get("file_name"):
            raise PermissionDenied()
        elif user_id_in_key != request.user.id:
            raise PermissionDenied()

        response = Response()
        response['X-Accel-Redirect'] = '/' + HIDDEN_REDIRECT_PATH + '/'
        response['redirect_uri'] = file_url_in_key

        return response
