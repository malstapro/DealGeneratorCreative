# Generated by Django 4.1.1 on 2022-09-26 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Deal",
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
                ("date", models.DateTimeField(auto_now_add=True)),
                ("entry_price", models.FloatField()),
                ("sell_price", models.FloatField()),
                ("profit", models.FloatField()),
            ],
        ),
    ]