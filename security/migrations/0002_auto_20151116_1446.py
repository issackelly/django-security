# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import security.models


class Migration(migrations.Migration):

    dependencies = [
        ('security', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passwordexpiry',
            name='password_expiry_date',
            field=models.DateTimeField(default=security.models.expiry, help_text=b"The date and time when the user's password expires. If this is empty, the password never expires.", null=True),
        ),
    ]
