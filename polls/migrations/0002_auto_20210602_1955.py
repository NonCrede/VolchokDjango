# Generated by Django 3.2.3 on 2021-06-02 13:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='number',
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
    ]
