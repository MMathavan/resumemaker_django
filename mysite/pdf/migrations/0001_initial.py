# Generated by Django 4.2.16 on 2024-11-29 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Profile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("email", models.CharField(max_length=100)),
                ("phone", models.IntegerField(max_length=100)),
                ("age", models.IntegerField(max_length=100)),
                ("summary", models.TextField(max_length=2000)),
                ("degree", models.CharField(max_length=100)),
                ("school", models.CharField(max_length=100)),
                ("university", models.CharField(max_length=200)),
                ("previous_work", models.TextField(max_length=1000)),
                ("skills", models.CharField(max_length=2000)),
            ],
        ),
    ]
