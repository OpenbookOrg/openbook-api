# Generated by Django 2.2.5 on 2020-01-20 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('openbook_circles', '0013_auto_20190414_2017'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='connectioncircle',
            index=models.Index(fields=['connection', 'circle'], name='openbook_ci_connect_da1cd9_idx'),
        ),
    ]
