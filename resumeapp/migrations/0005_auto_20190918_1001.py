# Generated by Django 2.1.1 on 2019-09-18 01:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resumeapp', '0004_resumelist_salary'),
    ]

    operations = [
        migrations.AddField(
            model_name='resumelist',
            name='email_address',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='resumelist',
            name='phone_number',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
