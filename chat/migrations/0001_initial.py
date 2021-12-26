# Generated by Django 3.2.6 on 2021-12-26 20:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('calendarSite', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=200)),
                ('author', models.CharField(default='', max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='作成日')),
                ('good_count', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='ReactionAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(default='', max_length=100)),
                ('answer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chat.answer')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=200)),
                ('author', models.CharField(default='', max_length=100)),
                ('resolved', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='作成日')),
                ('subject_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='calendarSite.subject')),
            ],
        ),
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=200)),
                ('action', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='作成日')),
                ('subject_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='calendarSite.subject')),
                ('task_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='calendarSite.task')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=200)),
                ('author', models.CharField(default='', max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='作成日')),
                ('subject_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='calendarSite.subject')),
            ],
        ),
        migrations.AddField(
            model_name='answer',
            name='question_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chat.question'),
        ),
    ]