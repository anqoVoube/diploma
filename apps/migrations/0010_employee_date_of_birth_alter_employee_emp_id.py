# Generated by Django 4.0.4 on 2022-05-26 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0009_alter_employee_emp_id_alter_employee_region'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='emp_id',
            field=models.CharField(default='emp611', max_length=70),
        ),
    ]
