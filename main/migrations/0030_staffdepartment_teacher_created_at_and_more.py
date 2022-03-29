# Generated by Django 4.0.3 on 2022-03-29 11:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0029_remove_subject_grade_remove_subject_teacher_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='StaffDepartment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_description', models.TextField()),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.department')),
            ],
        ),
        migrations.AddField(
            model_name='teacher',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='grade',
            name='student_count',
            field=models.PositiveSmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='result',
            name='pass_marks',
            field=models.FloatField(),
        ),
        migrations.RemoveField(
            model_name='staff',
            name='department',
        ),
        migrations.AddField(
            model_name='staff',
            name='department',
            field=models.ManyToManyField(through='main.StaffDepartment', to='main.department'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='salary',
            field=models.PositiveIntegerField(),
        ),
        migrations.AddField(
            model_name='staffdepartment',
            name='staff',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.staff'),
        ),
    ]
