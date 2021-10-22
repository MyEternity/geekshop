# Generated by Django 3.2.8 on 2021-10-22 13:44

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('users', '0003_auto_20211022_1005'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tagline', models.CharField(blank=True, max_length=128, verbose_name='Теги')),
                ('about', models.TextField(blank=True, null=True, verbose_name='О себе')),
                ('gender',
                 models.CharField(blank=True, choices=[('M', 'М'), ('W', 'Ж')], max_length=5, verbose_name='Пол')),
                (
                'user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
