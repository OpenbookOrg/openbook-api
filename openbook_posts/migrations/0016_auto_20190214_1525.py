# Generated by Django 2.1.5 on 2019-02-14 14:25

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('openbook_posts', '0015_post_community'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postimage',
            name='image',
            field=imagekit.models.fields.ProcessedImageField(null=True, upload_to='', verbose_name='image'),
        ),
    ]
