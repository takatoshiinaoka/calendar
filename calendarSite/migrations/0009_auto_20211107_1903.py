# Generated by Django 2.1.7 on 2021-11-07 10:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('calendarSite', '0008_auto_20211107_1901'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='subject_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='calendarSite.Subject'),
        ),
    ]