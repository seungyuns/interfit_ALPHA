# Generated by Django 2.1.1 on 2019-09-18 01:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('positionapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recruitlist',
            name='recruit_email',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='recruitlist',
            name='recruit_phone',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
