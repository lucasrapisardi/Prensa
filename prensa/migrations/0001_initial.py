# Generated by Django 4.1.1 on 2022-12-12 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="TensCis",
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
                ("cargaExerc", models.IntegerField()),
                ("nRebites", models.IntegerField()),
                ("pRebites", models.IntegerField()),
                ("dRebites", models.IntegerField()),
            ],
        ),
    ]
