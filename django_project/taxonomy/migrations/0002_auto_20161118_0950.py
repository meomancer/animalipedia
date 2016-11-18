# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taxonomy', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='additionalcharacteristic',
            old_name='name_english',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='additionaldescription',
            old_name='name_english',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='additionalcharacteristic',
            name='name_latin',
        ),
        migrations.RemoveField(
            model_name='additionaldescription',
            name='name_latin',
        ),
    ]
