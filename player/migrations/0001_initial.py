# Generated by Django 3.0.5 on 2020-04-16 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nume', models.CharField(max_length=255)),
                ('prenume', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('nume_utilizator', models.CharField(max_length=255)),
            ],
        ),
    ]
