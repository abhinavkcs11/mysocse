# Generated by Django 2.2.12 on 2021-06-05 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventsapp', '0003_alter_eventmodel_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventmodel',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
