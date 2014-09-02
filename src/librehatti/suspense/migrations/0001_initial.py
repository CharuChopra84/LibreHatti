# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=150)),
                ('phone', models.CharField(max_length=20, blank=True)),
                ('dean', models.CharField(max_length=50, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SuspenseClearance',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('suspense_id', models.IntegerField()),
                ('work_charge', models.IntegerField(null=True, blank=True)),
                ('labour_charge', models.IntegerField(null=True, blank=True)),
                ('car_taxi_charge', models.IntegerField(null=True, blank=True)),
                ('boring_charge_external', models.IntegerField(null=True, blank=True)),
                ('boring_charge_internal', models.IntegerField(null=True, blank=True)),
                ('lab_testing_staff', models.CharField(max_length=200)),
                ('field_testing_staff', models.CharField(max_length=200)),
                ('test_date', models.DateField(default=datetime.date.today)),
                ('clear_date', models.DateField(default=datetime.date.today)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProgrammeLetter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Address', models.CharField(max_length=500)),
                ('ClientName', models.CharField(max_length=200)),
                ('ClientContact', models.CharField(max_length=10)),
                ('Subject', models.CharField(max_length=200)),
                ('Staff', models.CharField(max_length=700)),
                ('Site_Venue', models.CharField(max_length=500)),
                ('Site_Date', models.DateField(default=datetime.date.today)),
                ('Site_Time', models.TimeField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TaDa',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('suspense', models.IntegerField()),
                ('departure_time_from_tcc', models.TimeField()),
                ('arrival_time_at_site', models.TimeField()),
                ('departure_time_from_site', models.TimeField()),
                ('arrival_time_at_tcc', models.TimeField()),
                ('tada_amount', models.IntegerField()),
                ('start_test_date', models.DateField()),
                ('end_test_date', models.DateField()),
                ('source_site', models.CharField(max_length=100)),
                ('testing_site', models.CharField(max_length=100)),
                ('testing_staff', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('department', models.ForeignKey(to='suspense.Department', to_field='id')),
                ('code', models.CharField(max_length=5)),
                ('name', models.CharField(max_length=50)),
                ('daily_income', models.IntegerField(blank=True)),
                ('position', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=75, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
