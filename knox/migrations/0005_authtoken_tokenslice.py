# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models

def clear_tokens(apps, schema_editor):
    Tokens = apps.get_model("knox", "AuthToken")
    Tokens.objects.all().delete()

class Migration(migrations.Migration):

    dependencies = [
        ('knox', '0004_authtoken_expires'),
    ]

    operations = [
        migrations.RunPython(clear_tokens),
        migrations.AddField(
            model_name='authtoken',
            name='token_slice',
            field=models.CharField(null=False, serialize=False, max_length=16, db_index=True),
        ),
    ]
