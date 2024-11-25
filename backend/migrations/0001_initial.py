# Generated by Django 5.1.3 on 2024-11-24 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Destination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('location', models.CharField(max_length=255)),
                ('country', models.CharField(max_length=100)),
                ('continent', models.CharField(max_length=100)),
                ('is_liked', models.BooleanField(default=False)),
            ],
        ),
    ]