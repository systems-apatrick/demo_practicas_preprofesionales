# Generated by Django 3.1.2 on 2020-10-28 02:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitter', '0002_auto_20201027_1907'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='consulted_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
