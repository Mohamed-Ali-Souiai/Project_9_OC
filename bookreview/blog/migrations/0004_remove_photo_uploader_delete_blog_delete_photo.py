# Generated by Django 4.1.1 on 2022-10-21 09:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0003_alter_review_body"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="photo",
            name="uploader",
        ),
        migrations.DeleteModel(
            name="Blog",
        ),
        migrations.DeleteModel(
            name="Photo",
        ),
    ]
