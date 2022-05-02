# Generated by Django 4.0.3 on 2022-04-28 06:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0004_alter_student_slug_alter_student_unique_together'),
        ('attendance', '0002_alter_attendance_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='attendance_student', to='student.student'),
        ),
    ]
