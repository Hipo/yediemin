from django.conf import settings
from rest_framework.authentication import SessionAuthentication

HIDDEN_REDIRECT_PATH = getattr(settings, "YEDIEMIN_HIDDEN_REDIRECT_PATH", "yediemin-files")
AUTHENTICATION_CLASS = getattr(settings, "YEDIEMIN_AUTHENTICATION_CLASS", SessionAuthentication)
EXPIRE_IN = getattr(settings, "YEDIEMIN_EXPIRE_IN", 2592000)
