# Generated by Django 5.0.4 on 2024-04-06 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
