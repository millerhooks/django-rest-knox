# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('knox', '0004_authtoken_expires'),
    ]

    operations = [
        migrations.AddField(
            model_name='authtoken',
            name='token_slice',
            field=models.CharField(null=False, serialize=False, max_length=16, db_index=True),
        ),
    ]
