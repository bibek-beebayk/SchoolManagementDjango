# Generated by Django 4.0.3 on 2022-03-27 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_assignment_grade_alter_exam_grade_alter_fee_grade'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='is_specially_abled',
            field=models.BooleanField(default=False, null=True, verbose_name='Is the student specially abled?'),
        ),
    ]