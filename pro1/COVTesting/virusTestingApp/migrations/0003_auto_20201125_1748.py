# Generated by Django 3.1.3 on 2020-11-25 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('virusTestingApp', '0002_auto_20201125_1635'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registereduser',
            name='address',
            field=models.CharField(max_length=60),
        ),
        migrations.AlterField(
            model_name='registereduser',
            name='age',
            field=models.CharField(max_length=60),
        ),
        migrations.AlterField(
            model_name='registereduser',
            name='email',
            field=models.CharField(max_length=60, unique=True),
        ),
        migrations.AlterField(
            model_name='registereduser',
            name='gender',
            field=models.CharField(max_length=60),
        ),
        migrations.AlterField(
            model_name='registereduser',
            name='name',
            field=models.CharField(max_length=60),
        ),
        migrations.AlterField(
            model_name='registereduser',
            name='postcode',
            field=models.CharField(max_length=60),
        ),
        migrations.AlterField(
            model_name='registereduser',
            name='testResult',
            field=models.CharField(max_length=60),
        ),
        migrations.AlterField(
            model_name='registereduser',
            name='ttn',
            field=models.CharField(max_length=60, unique=True),
        ),
    ]
