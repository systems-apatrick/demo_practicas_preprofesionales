# Generated by Django 3.1.2 on 2020-10-31 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mercadolibre', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mercadolibre',
            name='id',
        ),
        migrations.AlterField(
            model_name='mercadolibre',
            name='consulted_at',
            field=models.DateTimeField(auto_now=True, primary_key=True, serialize=False),
        ),
    ]