import os
import uuid

from django.db import models

from .fields import EditorMdFormField


class EditorMdField(models.TextField):
    def formfield(self, **kwargs):
        defaults = {'form_class': EditorMdFormField}
        defaults.update(kwargs)
        return super(EditorMdField, self).formfield(**defaults)


def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('editormd/', filename)


class EditormdImage(models.Model):
    image_file = models.FileField(upload_to=get_file_path)
    author = models.CharField(max_length=128)
    created = models.DateTimeField(auto_now_add=True)
