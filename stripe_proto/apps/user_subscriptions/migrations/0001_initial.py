# Generated by Django 3.2.16 on 2023-01-11 16:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('backends', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TeamMembership',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='TeamSubscription',
            fields=[
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('members', models.ManyToManyField(related_name='team_accounts', through='user_subscriptions.TeamMembership', to=settings.AUTH_USER_MODEL)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('subscription', models.ForeignKey(blank=True, help_text="The account's Subscription object, if it exists", null=True, on_delete=django.db.models.deletion.CASCADE, to='backends.subscription')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='teammembership',
            name='team_account',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_subscriptions.teamsubscription'),
        ),
        migrations.AddField(
            model_name='teammembership',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='IndividualSubscription',
            fields=[
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('subscription', models.ForeignKey(blank=True, help_text="The account's Subscription object, if it exists", null=True, on_delete=django.db.models.deletion.CASCADE, to='backends.subscription')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
