# Generated by Django 4.0.3 on 2022-03-28 07:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0024_alter_result_percentage'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='assignment',
            options={},
        ),
        migrations.AlterModelOptions(
            name='department',
            options={},
        ),
        migrations.AlterModelOptions(
            name='exam',
            options={},
        ),
        migrations.AlterModelOptions(
            name='fee',
            options={},
        ),
        migrations.AlterModelOptions(
            name='grade',
            options={},
        ),
        migrations.AlterModelOptions(
            name='result',
            options={},
        ),
        migrations.AlterModelOptions(
            name='staff',
            options={},
        ),
        migrations.AlterModelOptions(
            name='student',
            options={},
        ),
        migrations.AlterModelOptions(
            name='subject',
            options={},
        ),
        migrations.AlterModelOptions(
            name='teacher',
            options={},
        ),
        migrations.RenameField(
            model_name='student',
            old_name='enrolled_class',
            new_name='grade',
        ),
        migrations.RenameField(
            model_name='subject',
            old_name='subject_teacher',
            new_name='teacher',
        ),
        migrations.AlterModelTable(
            name='assignment',
            table=None,
        ),
        migrations.AlterModelTable(
            name='department',
            table=None,
        ),
        migrations.AlterModelTable(
            name='exam',
            table=None,
        ),
        migrations.AlterModelTable(
            name='fee',
            table=None,
        ),
        migrations.AlterModelTable(
            name='grade',
            table=None,
        ),
        migrations.AlterModelTable(
            name='result',
            table=None,
        ),
        migrations.AlterModelTable(
            name='staff',
            table=None,
        ),
        migrations.AlterModelTable(
            name='student',
            table=None,
        ),
        migrations.AlterModelTable(
            name='subject',
            table=None,
        ),
        migrations.AlterModelTable(
            name='teacher',
            table=None,
        ),
    ]
