# Generated by Django 4.2.16 on 2024-11-29 10:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("pdf", "0002_remove_profile_age_remove_profile_phone"),
    ]

    operations = [
        migrations.DeleteModel(name="Profile",),
    ]
