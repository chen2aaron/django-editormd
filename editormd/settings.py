from django.conf import settings

UPLOAD_TO = getattr(settings, 'EDITORMD_UPLOAD_TO', 'uploads/editormd')
