# Generated by Django 4.1.1 on 2022-09-26 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("deals", "0002_admin_panel"),
    ]

    operations = [
        migrations.AddField(
            model_name="deal",
            name="crypto",
            field=models.CharField(
                default=1, max_length=100, verbose_name="Название Крипты"
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="admin_panel",
            name="delay",
            field=models.IntegerField(
                default=1, verbose_name="Интервал генерации сделок"
            ),
        ),
    ]
