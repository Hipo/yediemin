from rest_framework.exceptions import PermissionDenied
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from django.core import signing

from yediemin.settings import HIDDEN_REDIRECT_PATH, AUTHENTICATION_CLASS


class YedieminView(GenericAPIView):
    permission_classes = []
    authentication_classes = [AUTHENTICATION_CLASS]

    def get(self, request, *args, **kwargs):
        key = request.query_params.get("key", "")
        values_in_key = signing.loads(key)

        file_name_in_key = values_in_key["file_name"]
        file_url_in_key = values_in_key["file_url"]
        user_id_in_key = values_in_key["user_id"]

        if file_name_in_key != kwargs.get("file_name"):
            raise PermissionDenied()
        elif user_id_in_key != request.user.id:
            raise PermissionDenied()

        response = Response()
        response['X-Accel-Redirect'] = '/' + HIDDEN_REDIRECT_PATH + '/'
        response['redirect_uri'] = file_url_in_key

        return response
