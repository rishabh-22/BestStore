# Generated by Django 2.2.1 on 2019-06-12 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0002_useraddress'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraddress',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='useraddress',
            name='label',
            field=models.CharField(default='Home', max_length=20),
        ),
        migrations.AddField(
            model_name='useraddress',
            name='pincode',
            field=models.IntegerField(max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='useraddress',
            name='landmark',
            field=models.CharField(max_length=50, null=True),
        ),
    ]