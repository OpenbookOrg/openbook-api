# Generated by Django 2.2 on 2019-05-19 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('openbook_moderation', '0004_auto_20190518_1948'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moderatedobject',
            name='object_audit_snapshot',
            field=models.TextField(null=True, verbose_name='object_audit_snapshot'),
        ),
    ]
