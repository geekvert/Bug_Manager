# Generated by Django 3.0.5 on 2020-05-18 09:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0006_auto_20200517_1419'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to='backend/bug_images/<property object at 0x7fcfbec0f458>'),
        ),
    ]