# Generated by Django 3.2.5 on 2021-07-26 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='short_desc',
            field=models.CharField(default='', max_length=300),
        ),
    ]
