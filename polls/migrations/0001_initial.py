# Generated by Django 3.2.3 on 2021-09-07 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=200, verbose_name='Вопрос:')),
                ('question_number', models.PositiveIntegerField(verbose_name='Номер:')),
            ],
        ),
    ]