# Generated by Django 5.0.2 on 2024-03-06 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_room_checkout'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='available',
            field=models.BooleanField(default=True),
        ),
    ]
