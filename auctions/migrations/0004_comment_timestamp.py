# Generated by Django 4.2.1 on 2023-06-04 19:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("auctions", "0003_comment"),
    ]

    operations = [
        migrations.AddField(
            model_name="comment",
            name="timestamp",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]