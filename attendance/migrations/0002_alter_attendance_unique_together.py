# Generated by Django 4.0.3 on 2022-04-28 05:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0004_alter_student_slug_alter_student_unique_together'),
        ('attendance', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='attendance',
            unique_together={('date', 'student')},
        ),
    ]
