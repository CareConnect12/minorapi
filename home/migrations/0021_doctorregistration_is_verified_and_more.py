# Generated by Django 5.1 on 2025-01-19 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0020_alter_registration_token'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctorregistration',
            name='is_verified',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='doctorregistration',
            name='token',
            field=models.TextField(default=''),
        ),
    ]
