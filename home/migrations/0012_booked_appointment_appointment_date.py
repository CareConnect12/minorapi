# Generated by Django 5.1 on 2024-11-14 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_booked_appointment'),
    ]

    operations = [
        migrations.AddField(
            model_name='booked_appointment',
            name='appointment_date',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
