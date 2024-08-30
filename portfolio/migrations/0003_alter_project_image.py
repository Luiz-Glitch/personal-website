# Generated by Django 5.1 on 2024-08-30 21:18

import django.utils.timezone
import portfolio.utils
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("portfolio", "0002_alter_project_end_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="project",
            name="image",
            field=models.ImageField(
                default=django.utils.timezone.now,
                upload_to=portfolio.utils.upload_project_image,
            ),
            preserve_default=False,
        ),
    ]
