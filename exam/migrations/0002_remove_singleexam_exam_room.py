# Generated by Django 4.0.3 on 2022-04-28 11:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='singleexam',
            name='exam_room',
        ),
    ]