# Generated by Django 2.0.6 on 2019-02-28 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cwApp', '0002_auto_20190228_1731'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newcarmodel',
            name='modelYear',
            field=models.IntegerField(default=2019),
        ),
    ]