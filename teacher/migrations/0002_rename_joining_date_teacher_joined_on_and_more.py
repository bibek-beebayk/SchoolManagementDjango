# Generated by Django 4.0.3 on 2022-04-05 11:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='teacher',
            old_name='joining_date',
            new_name='joined_on',
        ),
        migrations.RenameField(
            model_name='teacher',
            old_name='first_name',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='middle_name',
        ),
    ]
