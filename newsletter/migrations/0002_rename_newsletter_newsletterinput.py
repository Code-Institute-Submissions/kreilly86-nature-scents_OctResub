# Generated by Django 3.2.15 on 2022-10-15 18:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Newsletter',
            new_name='NewsletterInput',
        ),
    ]
