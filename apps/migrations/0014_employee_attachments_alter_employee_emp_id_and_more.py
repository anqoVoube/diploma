# Generated by Django 4.0.4 on 2022-05-26 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0013_remove_employee_passport_image_alter_employee_emp_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='attachments',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='emp_id',
            field=models.CharField(default='emp763', max_length=70),
        ),
        migrations.DeleteModel(
            name='Attachments',
        ),
    ]