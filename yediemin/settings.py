from django.conf import settings
from rest_framework.authentication import SessionAuthentication

HIDDEN_REDIRECT_PATH = getattr(settings, "YEDIEMIN_HIDDEN_REDIRECT_PATH", "yediemin-files")
AUTHENTICATION_CLASSES = getattr(settings, "YEDIEMIN_AUTHENTICATION_CLASSES", [SessionAuthentication])
EXPIRE_IN = getattr(settings, "YEDIEMIN_EXPIRE_IN", 604800)


if EXPIRE_IN > 604800:
    raise ValueError(
        "AuthorizationQueryParametersError: X-Amz-Expires must be less than a week (in seconds); that is,"
        " the given X-Amz-Expires must be less than 604800 seconds."
    )