# Generated by Django 4.0.2 on 2022-05-31 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restapi', '0005_sign'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sign',
            name='user',
        ),
        migrations.AddField(
            model_name='sign',
            name='user_name',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
    ]
