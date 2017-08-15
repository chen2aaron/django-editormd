# Django Editor md

>django-editormd package helps integrate [editor.md](https://github.com/pandao/editor.md) with Django.

## Getting started

Install the package:

  `pip install django-editormd`


Add `editormd` to INSTALLED_APPS in `settings.py`.


## Usage


1. Usage in models

```python
from editormd.models import EditorMdField


class Page(models.Model):
    content_editormd1 = EditorMdField()
```

2. OR Usage in forms

```python
from editormd.fields import EditorMdFormField


class PageForm(forms.ModelForm):
    content_editormd1 = EditorMdFormField()
    content_editormd2 = EditorMdFormField()
    content_editormd3 = EditorMdFormField()

    class Meta:
        model = Page
        fields = '__all__'


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    form = PageForm
```

## Settings

You can use the following settings in `settings.py`.

- EDITORMD_UPLOAD_TO
  set your upload path
  
- EDITORMD_WATERMARK
  default is false, if set True, you should set `EDITORMD_WATERMARK_TEXT='some string'`
  
- EDITORMD_UPLOAD_SUFFIX
  If you use `django-qiniu-storage`, maybe you will use watermark suffix.
