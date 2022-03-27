# Generated by Django 4.0.3 on 2022-03-27 11:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_delete_result'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='fee',
            options={'verbose_name_plural': 'Fees'},
        ),
        migrations.AlterField(
            model_name='fee',
            name='admission_fee',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_marks', models.IntegerField()),
                ('pass_marks', models.IntegerField()),
                ('percentage', models.PositiveBigIntegerField()),
                ('result', models.CharField(choices=[('P', 'Pass'), ('F', 'Fail')], max_length=1)),
                ('grade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.grade')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.student')),
            ],
            options={
                'verbose_name_plural': 'Results',
                'db_table': 'Results',
            },
        ),
    ]
