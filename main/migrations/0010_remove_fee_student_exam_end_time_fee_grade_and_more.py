# Generated by Django 4.0.3 on 2022-03-27 06:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_alter_teacher_options_assignment_short_title_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fee',
            name='student',
        ),
        migrations.AddField(
            model_name='exam',
            name='end_time',
            field=models.TimeField(null=True, verbose_name='Ending Time'),
        ),
        migrations.AddField(
            model_name='fee',
            name='grade',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.grade'),
        ),
        migrations.AlterField(
            model_name='assignment',
            name='short_title',
            field=models.CharField(max_length=256, null=True, verbose_name='Short Title'),
        ),
        migrations.AlterField(
            model_name='assignment',
            name='submission_date',
            field=models.DateField(verbose_name='Submission Due Date'),
        ),
        migrations.AlterField(
            model_name='department',
            name='name',
            field=models.CharField(max_length=256, verbose_name='Department Name'),
        ),
        migrations.AlterField(
            model_name='exam',
            name='exam_date',
            field=models.DateField(verbose_name='Date of Exam'),
        ),
        migrations.AlterField(
            model_name='exam',
            name='full_marks',
            field=models.PositiveSmallIntegerField(verbose_name='Full Marks'),
        ),
        migrations.AlterField(
            model_name='exam',
            name='pass_marks',
            field=models.PositiveSmallIntegerField(verbose_name='Pass Marks'),
        ),
        migrations.AlterField(
            model_name='exam',
            name='room_no',
            field=models.CharField(max_length=256, verbose_name='Room Number'),
        ),
        migrations.AlterField(
            model_name='exam',
            name='start_time',
            field=models.TimeField(verbose_name='Starting Time'),
        ),
        migrations.AlterField(
            model_name='fee',
            name='fee_type',
            field=models.CharField(choices=[('A', 'Admission Fee'), ('T', 'Transportation Fee'), ('M', 'Monthly Fee'), ('S', 'Sports, ECA, and Stationery'), ('H', 'Hostel Fee'), ('O', 'Other')], max_length=1, verbose_name='Type of Fee'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='dept',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.department', verbose_name='Department'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='first_name',
            field=models.CharField(max_length=256, verbose_name='First Name'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='job_designation',
            field=models.CharField(max_length=256, verbose_name='Job Designation'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='joining_date',
            field=models.DateField(verbose_name='Joining Date'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='last_name',
            field=models.CharField(max_length=256, verbose_name='Last Namr'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='middle_name',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Middle Name'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='phone',
            field=models.CharField(max_length=10, verbose_name='Phone Number'),
        ),
        migrations.AlterField(
            model_name='student',
            name='admission_date',
            field=models.DateField(verbose_name='Admission Date'),
        ),
        migrations.AlterField(
            model_name='student',
            name='dob',
            field=models.DateField(verbose_name='Date of Birth'),
        ),
        migrations.AlterField(
            model_name='student',
            name='enrolled_class',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.grade', verbose_name='Enrolled Class'),
        ),
        migrations.AlterField(
            model_name='student',
            name='first_name',
            field=models.CharField(max_length=256, verbose_name='First Name'),
        ),
        migrations.AlterField(
            model_name='student',
            name='guardian_address',
            field=models.CharField(max_length=256, verbose_name="GUardian's Address"),
        ),
        migrations.AlterField(
            model_name='student',
            name='guardian_name',
            field=models.CharField(max_length=256, verbose_name="Guardian's Name"),
        ),
        migrations.AlterField(
            model_name='student',
            name='guardian_phone',
            field=models.CharField(max_length=10, verbose_name="Guardian's Phone Number"),
        ),
        migrations.AlterField(
            model_name='student',
            name='guardian_profession',
            field=models.CharField(max_length=256, verbose_name="Guardian's Profession"),
        ),
        migrations.AlterField(
            model_name='student',
            name='last_name',
            field=models.CharField(max_length=256, verbose_name='Last Name'),
        ),
        migrations.AlterField(
            model_name='student',
            name='middle_name',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Middle Name'),
        ),
        migrations.AlterField(
            model_name='student',
            name='previous_school',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Previous School (if any)'),
        ),
        migrations.AlterField(
            model_name='student',
            name='roll_no',
            field=models.PositiveSmallIntegerField(verbose_name='Roll Number'),
        ),
        migrations.AlterField(
            model_name='subject',
            name='subject_teacher',
            field=models.ManyToManyField(to='main.teacher', verbose_name='Subject Teacher'),
        ),
        migrations.AlterField(
            model_name='subject',
            name='text_book',
            field=models.CharField(max_length=256, null=True, verbose_name='Text Book'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='dob',
            field=models.DateField(verbose_name='Date of Birth'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='first_name',
            field=models.CharField(max_length=256, verbose_name='First Name'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='joining_date',
            field=models.DateField(verbose_name='Joining Date'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='last_name',
            field=models.CharField(max_length=256, verbose_name='Last Name'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='middle_name',
            field=models.CharField(blank=True, max_length=56, null=True, verbose_name='Middle Name'),
        ),
    ]
