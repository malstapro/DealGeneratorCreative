# Generated by Django 4.1.1 on 2022-09-26 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("deals", "0008_deal_exchange"),
    ]

    operations = [
        migrations.AlterField(
            model_name="deal",
            name="exchange",
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
    ]
