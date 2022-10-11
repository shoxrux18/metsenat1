# Generated by Django 4.0.6 on 2022-09-13 16:56

import api.decorators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_student_passport'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='passport',
            field=models.FileField(upload_to=api.decorators.UploadTo('passport')),
        ),
    ]
