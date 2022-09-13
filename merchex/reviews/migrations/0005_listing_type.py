# Generated by Django 4.1.1 on 2022-09-19 23:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("reviews", "0004_listing_band_listing_description_listing_sold_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="listing",
            name="type",
            field=models.CharField(
                choices=[
                    ("R", "Records"),
                    ("C", "Clothing"),
                    ("P", "Posters"),
                    ("M", "Music"),
                ],
                default="R",
                max_length=5,
            ),
            preserve_default=False,
        ),
    ]