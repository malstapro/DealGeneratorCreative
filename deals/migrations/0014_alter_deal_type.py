# Generated by Django 4.1.1 on 2022-10-01 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("deals", "0013_deal_type"),
    ]

    operations = [
        migrations.AlterField(
            model_name="deal",
            name="type",
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
    ]
