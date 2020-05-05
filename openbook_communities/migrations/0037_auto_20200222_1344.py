# Generated by Django 2.2.5 on 2020-02-22 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('openbook_communities', '0036_delete_trendingcommunity'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='community',
            index=models.Index(fields=['activity_score'], name='openbook_co_activit_07d4ba_idx'),
        ),
    ]
