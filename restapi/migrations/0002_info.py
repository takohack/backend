# Generated by Django 4.0.2 on 2022-04-14 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restapi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('courseName', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('courseId', models.CharField(blank=True, default='', max_length=10, null=True)),
                ('coursechapters', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('coursehomework', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('coursenotice', models.CharField(blank=True, default='', max_length=200, null=True)),
            ],
        ),
    ]
