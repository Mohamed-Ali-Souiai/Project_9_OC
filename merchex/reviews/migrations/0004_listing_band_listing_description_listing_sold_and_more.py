# Generated by Django 4.1.1 on 2022-09-19 22:17

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("reviews", "0003_band_active_band_biography_band_genre_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="listing",
            name="band",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="reviews.band",
            ),
        ),
        migrations.AddField(
            model_name="listing",
            name="description",
            field=models.CharField(default="", max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="listing",
            name="sold",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="listing",
            name="year",
            field=models.IntegerField(
                null=True,
                validators=[
                    django.core.validators.MinValueValidator(1900),
                    django.core.validators.MaxValueValidator(2022),
                ],
            ),
        ),
    ]