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
