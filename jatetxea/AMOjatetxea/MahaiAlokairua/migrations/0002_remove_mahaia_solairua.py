# Generated by Django 3.1.4 on 2023-10-11 06:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MahaiAlokairua', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mahaia',
            name='solairua',
        ),
    ]