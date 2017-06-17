from django.db import models
from .fields import EditorMdFormField


class EditorMdField(models.TextField):
    def formfield(self, **kwargs):
        defaults = {'form_class': EditorMdFormField}
        defaults.update(kwargs)
        return super(EditorMdField, self).formfield(**defaults)
