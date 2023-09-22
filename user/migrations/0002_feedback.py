# Generated by Django 3.0.5 on 2020-11-25 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('placename', models.CharField(max_length=100)),
                ('package', models.CharField(max_length=100)),
                ('rating', models.CharField(max_length=200)),
                ('review', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'userfeedback',
            },
        ),
    ]