# Generated by Django 2.2.3 on 2019-07-29 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_auto_20190729_0921'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pessoa',
            name='password',
            field=models.CharField(max_length=255, verbose_name='Password'),
        ),
    ]