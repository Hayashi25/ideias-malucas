# Generated by Django 2.2.3 on 2019-07-26 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pessoa',
            name='biografia',
            field=models.TextField(blank=True, null=True),
        ),
    ]
