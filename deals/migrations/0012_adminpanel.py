# Generated by Django 4.1.1 on 2022-09-30 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("deals", "0011_delete_admin_panel"),
    ]

    operations = [
        migrations.CreateModel(
            name="AdminPanel",
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
                ("deal", models.IntegerField(default=200)),
                ("profit_all", models.FloatField(default=0)),
            ],
        ),
    ]
