# Generated by Django 4.0.3 on 2022-03-29 08:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0026_remove_staff_dept_remove_subject_teacher_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='teacher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='main.teacher'),
        ),
        migrations.AddField(
            model_name='subject',
            name='textbook',
            field=models.CharField(max_length=256, null=True),
        ),
    ]
