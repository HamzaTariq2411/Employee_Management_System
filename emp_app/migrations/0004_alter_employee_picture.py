# Generated by Django 4.2.3 on 2023-08-23 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emp_app', '0003_alter_employee_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='employee_pictures'),
        ),
    ]
