# Generated by Django 3.2.7 on 2021-09-20 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20210920_0943'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productcategory',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
