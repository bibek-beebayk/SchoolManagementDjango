# Generated by Django 4.0.4 on 2022-05-31 10:34

from django.db import migrations
import django_quill.fields


class Migration(migrations.Migration):

    dependencies = [
        ('assignment', '0003_alter_assignment_posted_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='description',
            field=django_quill.fields.QuillField(blank=True, null=True),
        ),
    ]
