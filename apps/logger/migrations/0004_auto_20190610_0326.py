# Generated by Django 2.1.5 on 2019-06-10 00:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logger', '0003_auto_20190610_0324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log',
            name='method',
            field=models.CharField(max_length=255, verbose_name='HTTP метод'),
        ),
    ]