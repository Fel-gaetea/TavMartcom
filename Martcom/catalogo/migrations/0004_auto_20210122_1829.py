# Generated by Django 3.1.5 on 2021-01-22 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0003_auto_20210122_1824'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='apell',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='nom',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='rut',
            field=models.CharField(max_length=10, primary_key=True, serialize=False),
        ),
    ]