# Generated by Django 5.0.3 on 2024-08-13 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bapp', '0003_coach_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='player',
            fields=[
                ('p_id', models.AutoField(primary_key=True, serialize=False)),
                ('playername', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=50)),
                ('mobileno', models.CharField(max_length=20)),
                ('birthdate', models.DateField()),
                ('gender', models.CharField(max_length=10)),
                ('height', models.CharField(max_length=15)),
                ('weight', models.CharField(max_length=15)),
                ('position', models.CharField(max_length=20)),
                ('joindate', models.DateField()),
                ('enddate', models.DateField()),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=15)),
                ('photo', models.ImageField(upload_to='player/')),
            ],
        ),
    ]
