# Generated by Django 3.1.4 on 2021-01-11 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeestate',
            name='EMPstate',
            field=models.IntegerField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='employeestate',
            name='RoomID',
            field=models.IntegerField(blank=True, max_length=100, null=True),
        ),
    ]
