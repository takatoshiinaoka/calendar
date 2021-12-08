# Generated by Django 2.1.5 on 2021-12-08 13:35

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Calendar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=200)),
                ('date', models.DateTimeField()),
                ('user', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('author', models.CharField(default='', max_length=100)),
                ('contents', models.CharField(blank=True, default='', max_length=100)),
                ('end', models.DateTimeField(default=datetime.datetime(2021, 12, 8, 13, 35, 32, 697413))),
                ('subject_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='calendarSite.Subject')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=200)),
                ('user_subject', models.CharField(max_length=200)),
                ('twitter_id', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='User_Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=200)),
                ('subject_id', models.CharField(max_length=200)),
                ('week', models.CharField(max_length=200)),
                ('period', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='User_Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=200)),
                ('task_id', models.CharField(max_length=200)),
                ('done', models.CharField(max_length=200)),
                ('notice', models.CharField(max_length=200)),
                ('howlong', models.CharField(max_length=200)),
            ],
        ),
    ]
