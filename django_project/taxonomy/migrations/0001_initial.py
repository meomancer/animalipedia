# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrative', '0002_data_migration'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdditionalCharacteristic',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name_english', models.CharField(max_length=128)),
                ('name_latin', models.CharField(max_length=128, null=True, blank=True)),
                ('description', models.TextField(null=True, blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AdditionalDescription',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name_english', models.CharField(max_length=128)),
                ('name_latin', models.CharField(max_length=128, null=True, blank=True)),
                ('description', models.TextField(null=True, blank=True)),
                ('image', models.ImageField(null=True, upload_to=b'/home/web/media/classification/characteristic/', blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name_latin', models.CharField(max_length=128)),
                ('name_english', models.CharField(max_length=128, null=True, blank=True)),
                ('description', models.TextField(null=True, blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Classification',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('classis', models.ForeignKey(to='taxonomy.Class')),
            ],
        ),
        migrations.CreateModel(
            name='Domain',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name_latin', models.CharField(max_length=128)),
                ('name_english', models.CharField(max_length=128, null=True, blank=True)),
                ('description', models.TextField(null=True, blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Family',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name_latin', models.CharField(max_length=128)),
                ('name_english', models.CharField(max_length=128, null=True, blank=True)),
                ('description', models.TextField(null=True, blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Genus',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name_latin', models.CharField(max_length=128)),
                ('name_english', models.CharField(max_length=128, null=True, blank=True)),
                ('description', models.TextField(null=True, blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Kingdom',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name_latin', models.CharField(max_length=128)),
                ('name_english', models.CharField(max_length=128, null=True, blank=True)),
                ('description', models.TextField(null=True, blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name_latin', models.CharField(max_length=128)),
                ('name_english', models.CharField(max_length=128, null=True, blank=True)),
                ('description', models.TextField(null=True, blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Phylum',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name_latin', models.CharField(max_length=128)),
                ('name_english', models.CharField(max_length=128, null=True, blank=True)),
                ('description', models.TextField(null=True, blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Species',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name_latin', models.CharField(max_length=128)),
                ('name_english', models.CharField(max_length=128, null=True, blank=True)),
                ('description', models.TextField(null=True, blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SubSpecies',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name_latin', models.CharField(max_length=128)),
                ('name_english', models.CharField(max_length=128, null=True, blank=True)),
                ('description', models.TextField(null=True, blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='classification',
            name='domain',
            field=models.ForeignKey(to='taxonomy.Domain'),
        ),
        migrations.AddField(
            model_name='classification',
            name='family',
            field=models.ForeignKey(to='taxonomy.Family'),
        ),
        migrations.AddField(
            model_name='classification',
            name='genus',
            field=models.ForeignKey(to='taxonomy.Genus'),
        ),
        migrations.AddField(
            model_name='classification',
            name='habitats',
            field=models.ManyToManyField(to='administrative.Country'),
        ),
        migrations.AddField(
            model_name='classification',
            name='kingdom',
            field=models.ForeignKey(to='taxonomy.Kingdom'),
        ),
        migrations.AddField(
            model_name='classification',
            name='order',
            field=models.ForeignKey(to='taxonomy.Order'),
        ),
        migrations.AddField(
            model_name='classification',
            name='phylum',
            field=models.ForeignKey(to='taxonomy.Phylum'),
        ),
        migrations.AddField(
            model_name='classification',
            name='species',
            field=models.ForeignKey(to='taxonomy.Species'),
        ),
        migrations.AddField(
            model_name='classification',
            name='subspecies',
            field=models.ForeignKey(blank=True, to='taxonomy.SubSpecies', null=True),
        ),
        migrations.AddField(
            model_name='additionaldescription',
            name='classification',
            field=models.ForeignKey(to='taxonomy.Classification'),
        ),
        migrations.AddField(
            model_name='additionalcharacteristic',
            name='classification',
            field=models.ForeignKey(to='taxonomy.Classification'),
        ),
    ]
