# Generated by Django 5.0.7 on 2024-07-27 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='coach',
            fields=[
                ('c_id', models.AutoField(primary_key=True, serialize=False)),
                ('firstname', models.CharField(max_length=20)),
                ('lastname', models.CharField(max_length=20)),
                ('birthdate', models.DateField()),
                ('gender', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=50)),
                ('address', models.CharField(max_length=100)),
                ('mobilenumber', models.CharField(max_length=11)),
                ('experience', models.CharField(max_length=15)),
                ('joindate', models.DateField()),
                ('enddate', models.DateField()),
                ('username', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
            ],
        ),
    ]
