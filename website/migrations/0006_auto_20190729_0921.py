# Generated by Django 2.2.3 on 2019-07-29 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_pessoa_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pessoa',
            name='password',
            field=models.CharField(max_length=200, verbose_name='Password'),
        ),
    ]
