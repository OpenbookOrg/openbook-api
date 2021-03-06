# Generated by Django 2.2.4 on 2019-08-08 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('openbook_notifications', '0012_auto_20190623_1657'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='notification_type',
            field=models.CharField(choices=[('PR', 'Post Reaction'), ('PC', 'Post Comment'), ('PCR', 'Post Comment Reply'), ('PCRA', 'Post Comment Reaction'), ('CR', 'Connection Request'), ('CC', 'Connection Confirmed'), ('F', 'Follow'), ('CI', 'Community Invite')], max_length=5),
        ),
    ]
