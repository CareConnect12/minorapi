# Generated by Django 5.1 on 2025-03-10 16:09

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=200)),
                ('user_id', models.PositiveIntegerField()),
                ('Doctor_id', models.PositiveIntegerField()),
                ('doctor_name', models.CharField(max_length=200)),
                ('booked_slot', models.CharField(max_length=50)),
                ('appointment_date', models.DateField()),
                ('purpose', models.TextField()),
                ('notes', models.TextField(blank=True, null=True)),
                ('payment_status', models.CharField(default='Pending', max_length=20)),
                ('status', models.CharField(default='Pending', max_length=200)),
                ('is_virtual', models.BooleanField(default=True)),
                ('meeting_link', models.URLField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='beds',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Hospital_name', models.CharField(max_length=300)),
                ('Hospital_id', models.TextField()),
                ('Bed_id', models.CharField(max_length=300, unique=True)),
                ('Ward_number', models.CharField(max_length=100)),
                ('Room_number', models.CharField(max_length=100)),
                ('Bed_type', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Booked_slot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appointment_date', models.DateField()),
                ('booked_slot', models.TextField()),
                ('Doctor_id', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Doctor_slot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slot_hour', models.PositiveIntegerField(default=0)),
                ('slot_type', models.CharField(max_length=200)),
                ('slot_duration', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='feed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('message', models.CharField(max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name='finalinformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Hospital_name', models.CharField(max_length=300)),
                ('Bed_id', models.CharField(max_length=300, unique=True)),
                ('Ward_number', models.IntegerField()),
                ('Room_number', models.IntegerField()),
                ('Disease', models.CharField(max_length=200)),
                ('Bed_type', models.CharField(max_length=300)),
                ('patient_name', models.CharField(max_length=200)),
                ('patient_gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Others', 'Others')], max_length=300)),
                ('patient_age', models.PositiveBigIntegerField()),
                ('address', models.TextField()),
                ('mobile_number', models.PositiveBigIntegerField()),
                ('current_medication', models.TextField()),
                ('allergies', models.TextField()),
                ('past_surgeries', models.TextField()),
                ('insurance_policy', models.TextField()),
                ('Policy_number', models.TextField()),
                ('special_request', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='hospitalinfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hospital_name', models.CharField(max_length=300)),
                ('hospital_image', models.ImageField(upload_to='hospital_images')),
                ('hospital_address', models.TextField()),
                ('hospital_details', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='patient_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Hospital_name', models.CharField(max_length=300)),
                ('Bed_id', models.CharField(max_length=300, unique=True)),
                ('Ward_number', models.IntegerField()),
                ('Room_number', models.IntegerField()),
                ('Disease', models.CharField(max_length=200)),
                ('Bed_type', models.CharField(max_length=300)),
                ('patient_name', models.CharField(max_length=200)),
                ('patient_gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Others', 'Others')], max_length=300)),
                ('patient_age', models.PositiveBigIntegerField()),
                ('address', models.TextField()),
                ('mobile_number', models.PositiveBigIntegerField()),
                ('current_medication', models.TextField()),
                ('allergies', models.TextField()),
                ('past_surgeries', models.TextField()),
                ('insurance_policy', models.TextField()),
                ('Policy_number', models.TextField()),
                ('special_request', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='DoctorRegistration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=200)),
                ('fathers_name', models.CharField(max_length=200)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=200)),
                ('email', models.CharField(max_length=200, unique=True)),
                ('passcode', models.TextField()),
                ('address1', models.TextField()),
                ('address2', models.TextField()),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(choices=[('Andhra Pradesh', 'Andhra Pradesh'), ('Arunachal Pradesh', 'Arunachal Pradesh'), ('Assam', 'Assam'), ('Bihar', 'Bihar'), ('Chhattisgarh', 'Chhattisgarh'), ('Goa', 'Goa'), ('Gujarat', 'Gujarat'), ('Haryana', 'Haryana'), ('Himachal Pradesh', 'Himachal Pradesh'), ('Jharkhand', 'Jharkhand'), ('Karnataka', 'Karnataka'), ('Kerala', 'Kerala'), ('Madhya Pradesh', 'Madhya Pradesh'), ('Maharashtra', 'Maharashtra'), ('Manipur', 'Manipur'), ('Meghalaya', 'Meghalaya'), ('Mizoram', 'Mizoram'), ('Nagaland', 'Nagaland'), ('Odisha', 'Odisha'), ('Punjab', 'Punjab'), ('Rajasthan', 'Rajasthan'), ('Sikkim', 'Sikkim'), ('Tamil Nadu', 'Tamil Nadu'), ('Telangana', 'Telangana'), ('Tripura', 'Tripura'), ('Uttar Pradesh', 'Uttar Pradesh'), ('Uttarakhand', 'Uttarakhand'), ('West Bengal', 'West Bengal'), ('Andaman and Nicobar Islands', 'Andaman and Nicobar Islands'), ('Chandigarh', 'Chandigarh'), (' Dadra and Nagar Haveli and Daman and Diu', ' Dadra and Nagar Haveli and Daman and Diu'), ('Lakshadweep', 'Lakshadweep'), ('Delhi', 'Delhi'), ('Puducherry', 'Puducherry')], max_length=50)),
                ('zip', models.IntegerField()),
                ('Morning_slot', models.BooleanField(default=False)),
                ('Evening_slot', models.BooleanField(default=False)),
                ('Night_slot', models.BooleanField(default=False)),
                ('Afternoon_slot', models.BooleanField(default=False)),
                ('login_status', models.IntegerField(default=0)),
                ('token', models.TextField(default='')),
                ('is_verified', models.BooleanField(default=False)),
                ('userRole', models.TextField(default='Doctor')),
                ('User', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=200)),
                ('fathers_name', models.CharField(max_length=200)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=200)),
                ('email', models.CharField(max_length=200, unique=True)),
                ('code', models.TextField()),
                ('address1', models.TextField()),
                ('address2', models.TextField()),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(choices=[('Andhra Pradesh', 'Andhra Pradesh'), ('Arunachal Pradesh', 'Arunachal Pradesh'), ('Assam', 'Assam'), ('Bihar', 'Bihar'), ('Chhattisgarh', 'Chhattisgarh'), ('Goa', 'Goa'), ('Gujarat', 'Gujarat'), ('Haryana', 'Haryana'), ('Himachal Pradesh', 'Himachal Pradesh'), ('Jharkhand', 'Jharkhand'), ('Karnataka', 'Karnataka'), ('Kerala', 'Kerala'), ('Madhya Pradesh', 'Madhya Pradesh'), ('Maharashtra', 'Maharashtra'), ('Manipur', 'Manipur'), ('Meghalaya', 'Meghalaya'), ('Mizoram', 'Mizoram'), ('Nagaland', 'Nagaland'), ('Odisha', 'Odisha'), ('Punjab', 'Punjab'), ('Rajasthan', 'Rajasthan'), ('Sikkim', 'Sikkim'), ('Tamil Nadu', 'Tamil Nadu'), ('Telangana', 'Telangana'), ('Tripura', 'Tripura'), ('Uttar Pradesh', 'Uttar Pradesh'), ('Uttarakhand', 'Uttarakhand'), ('West Bengal', 'West Bengal'), ('Andaman and Nicobar Islands', 'Andaman and Nicobar Islands'), ('Chandigarh', 'Chandigarh'), (' Dadra and Nagar Haveli and Daman and Diu', ' Dadra and Nagar Haveli and Daman and Diu'), ('Lakshadweep', 'Lakshadweep'), ('Delhi', 'Delhi'), ('Puducherry', 'Puducherry')], max_length=50)),
                ('zip', models.IntegerField()),
                ('token', models.TextField(default='')),
                ('is_verified', models.BooleanField(default=False)),
                ('userRole', models.TextField(default='User')),
                ('User', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
