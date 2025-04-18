# Generated by Django 5.0.3 on 2024-08-31 16:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bapp', '0014_assign_tb'),
    ]

    operations = [
        migrations.CreateModel(
            name='schedule1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=30)),
                ('Address', models.CharField(max_length=100)),
                ('startdate', models.DateField()),
                ('enddate', models.DateField()),
                ('starttime', models.CharField(max_length=20)),
                ('endtime', models.CharField(max_length=20)),
                ('role', models.CharField(max_length=30)),
                ('man_of_match', models.CharField(max_length=50)),
                ('coa_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='bapp.coach')),
                ('tm_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='bapp.team')),
            ],
        ),
    ]
