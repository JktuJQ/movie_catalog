# Generated by Django 5.1.4 on 2024-12-09 16:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_alter_choice_options_alter_poll_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vote',
            name='poll',
        ),
    ]
