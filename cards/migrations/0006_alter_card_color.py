# Generated by Django 5.0.4 on 2024-04-08 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0005_alter_card_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='color',
            field=models.IntegerField(choices=[(0, 'petal'), (1, 'poppy'), (2, 'stem'), (3, 'green')]),
        ),
    ]