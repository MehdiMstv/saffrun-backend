# Generated by Django 3.2.10 on 2021-12-24 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile', '0003_auto_20211223_1204'),
    ]

    operations = [
        migrations.AddField(
            model_name='employeeprofile',
            name='gender',
            field=models.CharField(choices=[('M', 'male'), ('F', 'female'), ('N', 'not specified')], default='N', max_length=1),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='gender',
            field=models.CharField(choices=[('M', 'male'), ('F', 'female'), ('N', 'not specified')], default='N', max_length=1),
        ),
    ]
