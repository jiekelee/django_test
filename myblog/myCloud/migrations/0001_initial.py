# Generated by Django 2.0.5 on 2018-05-05 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='fileModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('myfile', models.FileField(upload_to='upload')),
                ('upload_date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]