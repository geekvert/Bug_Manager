# Generated by Django 3.0.5 on 2020-06-03 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_auto_20200603_1327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to='backend/bug_images/<django.db.models.query_utils.DeferredAttribute object at 0x7fd6b06bbcc0>'),
        ),
    ]
