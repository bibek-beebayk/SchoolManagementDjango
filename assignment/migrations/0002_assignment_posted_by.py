# Generated by Django 4.0.3 on 2022-04-22 07:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0003_alter_teacher_dob_alter_teacher_email_and_more'),
        ('assignment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignment',
            name='posted_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='teacher.teacher'),
        ),
    ]
