# Generated by Django 3.1.6 on 2021-04-29 00:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('JMList', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='text',
            field=models.TextField(default=''),
        ),
    ]