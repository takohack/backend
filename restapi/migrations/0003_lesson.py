# Generated by Django 4.0.2 on 2022-04-16 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restapi', '0002_info'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lessonbelong', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('lessonname', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('lessonexrcise', models.CharField(blank=True, default='', max_length=400, null=True)),
                ('lessonreference', models.CharField(blank=True, default='', max_length=400, null=True)),
                ('lessonhomework', models.CharField(blank=True, default='', max_length=400, null=True)),
            ],
        ),
    ]