# Generated by Django 2.1.3 on 2020-09-24 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SendSms',
            fields=[
                ('phone_number', models.CharField(max_length=11, primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'phone_numbers',
            },
        ),
    ]