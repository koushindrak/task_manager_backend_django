# Generated by Django 4.1.7 on 2023-04-11 10:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('LabelApp', '0001_initial'),
        ('TaskApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LabelsTasks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_by', models.CharField(blank=True, default='system', max_length=255, null=True)),
                ('updated_by', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('labels', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LabelApp.labels')),
                ('tasks', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TaskApp.tasks')),
            ],
            options={
                'db_table': 'labels_tasks',
            },
        ),
    ]
