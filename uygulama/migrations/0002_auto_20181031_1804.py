# Generated by Django 2.1.2 on 2018-10-31 18:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uygulama', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='date',
            new_name='dateet',
        ),
    ]