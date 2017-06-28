# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import editormd.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EditormdImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('image_file', models.FileField(upload_to=editormd.models.get_file_path)),
                ('author', models.CharField(max_length=128)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
