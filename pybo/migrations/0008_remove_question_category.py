# Generated by Django 3.1.3 on 2021-03-11 14:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0007_question_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='category',
        ),
    ]