from django.conf import settings

HIDDEN_REDIRECT_PATH = getattr(settings, "YEDIEMIN_HIDDEN_REDIRECT_PATH", "yediemin-files")
