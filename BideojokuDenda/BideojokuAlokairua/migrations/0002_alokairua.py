# Generated by Django 4.2.5 on 2023-10-04 18:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('BideojokuAlokairua', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alokairua',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bezeroa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BideojokuAlokairua.bezeroa')),
                ('bideojokua', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BideojokuAlokairua.bideojokua')),
            ],
        ),
    ]
