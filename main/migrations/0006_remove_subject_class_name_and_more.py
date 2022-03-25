# Generated by Django 4.0.3 on 2022-03-25 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_subject_class_name_subject_text_book'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subject',
            name='class_name',
        ),
        migrations.RemoveField(
            model_name='subject',
            name='subject_teacher',
        ),
        migrations.AddField(
            model_name='subject',
            name='subject_teacher',
            field=models.ManyToManyField(to='main.teacher'),
        ),
    ]