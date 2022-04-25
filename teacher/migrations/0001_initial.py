# Generated by Django 4.0.3 on 2022-04-04 11:13

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=256)),
                ('middle_name', models.CharField(blank=True, max_length=56, null=True)),
                ('last_name', models.CharField(max_length=256)),
                ('mobile_number', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=256)),
                ('email', models.EmailField(max_length=254)),
                ('joining_date', models.DateField()),
                ('salary', models.PositiveIntegerField()),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=1)),
                ('specialization', models.CharField(max_length=256)),
                ('proficient_subjects', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=256), default=list, size=None)),
                ('dob', models.DateField(verbose_name='Date of Birth')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]