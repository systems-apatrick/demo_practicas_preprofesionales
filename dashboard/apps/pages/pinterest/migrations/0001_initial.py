# Generated by Django 3.1.2 on 2020-11-16 22:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductoPinterest',
            fields=[
                ('fecha_consulta', models.DateTimeField(auto_now=True)),
                ('titulo', models.CharField(max_length=200)),
                ('url', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=200)),
                ('url_imagen', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ProductoPinterestComentario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comentario', models.CharField(max_length=600)),
                ('url', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pinterest.productopinterest')),
            ],
        ),
    ]
