# Generated by Django 2.2.5 on 2019-11-26 17:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('openbook_communities', '0028_auto_20190606_0944'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommunityNotificationsSubscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('community', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notifications_subscriptions', to='openbook_communities.Community')),
                ('subscriber', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='community_notifications_subscriptions', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('community', 'subscriber')},
            },
        ),
    ]
