# Generated by Django 4.1.1 on 2022-09-07 16:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_student_address_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='University',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('university_cart', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'University',
                'verbose_name_plural': 'Universities',
            },
        ),
        migrations.AlterField(
            model_name='student',
            name='university',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='api.university'),
        ),
    ]