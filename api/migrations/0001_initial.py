# Generated by Django 4.0.6 on 2022-09-12 18:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
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
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('passport_number', models.CharField(max_length=255, unique=True)),
                ('address', models.CharField(max_length=255)),
                ('agree_with_agreement', models.BooleanField()),
                ('passport', models.FileField(upload_to='uploads/')),
                ('university_cert', models.FileField(blank=True, null=True, upload_to='uploads/%Y/%m/%d')),
                ('photo', models.FileField(blank=True, null=True, upload_to='uploads/%Y/%m/%d')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
                ('university', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.university')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Sponsor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('passport_number', models.CharField(blank=True, max_length=255, null=True, unique=True)),
                ('address', models.CharField(max_length=255, null=True)),
                ('agree_with_agreement', models.BooleanField(default=False)),
                ('passport', models.FileField(blank=True, null=True, upload_to='uploads/%Y/%m/%d')),
                ('photo', models.FileField(blank=True, null=True, upload_to='uploads/%Y/%m/%d')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.student')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
