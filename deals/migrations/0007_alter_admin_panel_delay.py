# Generated by Django 4.1.1 on 2022-09-26 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("deals", "0006_deal_event"),
    ]

    operations = [
        migrations.AlterField(
            model_name="admin_panel",
            name="delay",
            field=models.IntegerField(
                default=180, verbose_name="Интервал генерации сделок"
            ),
        ),
    ]
