# Generated by Django 4.0.3 on 2022-03-29 08:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0025_alter_assignment_options_alter_department_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='staff',
            name='dept',
        ),
        migrations.RemoveField(
            model_name='subject',
            name='teacher',
        ),
        migrations.RemoveField(
            model_name='subject',
            name='text_book',
        ),
        migrations.AddField(
            model_name='staff',
            name='department',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='main.department', verbose_name='Department'),
        ),
        migrations.AlterField(
            model_name='assignment',
            name='grade',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='main.grade'),
        ),
        migrations.AlterField(
            model_name='assignment',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.subject'),
        ),
        migrations.AlterField(
            model_name='exam',
            name='grade',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='main.grade'),
        ),
        migrations.AlterField(
            model_name='exam',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.subject'),
        ),
        migrations.AlterField(
            model_name='grade',
            name='class_teacher',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.PROTECT, to='main.teacher'),
        ),
        migrations.AlterField(
            model_name='student',
            name='grade',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='main.grade', verbose_name='Enrolled Class'),
        ),
        migrations.CreateModel(
            name='Mark',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_mark', models.PositiveSmallIntegerField(default=100)),
                ('pass_mark', models.PositiveSmallIntegerField(default=40)),
                ('obtained_mark', models.PositiveSmallIntegerField()),
                ('result', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to='main.result')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.subject')),
            ],
        ),
    ]
