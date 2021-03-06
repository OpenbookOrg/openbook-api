# Generated by Django 2.2.12 on 2020-10-17 16:00

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('openbook_posts', '0068_profilepostscommunityexclusion'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('link', models.TextField(max_length=5000)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_links', to='openbook_posts.Post')),
            ],
        ),
    ]
