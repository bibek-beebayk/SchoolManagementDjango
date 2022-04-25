# Generated by Django 4.0.3 on 2022-04-04 11:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('grade', '0001_initial'),
        ('subject', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exam_date', models.DateField()),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField(null=True)),
                ('full_marks', models.PositiveSmallIntegerField()),
                ('pass_marks', models.PositiveSmallIntegerField()),
                ('room_no', models.CharField(max_length=256)),
                ('description', models.TextField(blank=True, null=True)),
                ('grade', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='exam', to='grade.grade')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='subject.subject')),
            ],
        ),
    ]