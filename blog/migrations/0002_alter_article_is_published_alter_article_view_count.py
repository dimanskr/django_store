# Generated by Django 5.1.1 on 2024-10-07 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="article",
            name="is_published",
            field=models.BooleanField(default=True, verbose_name="опубликовано"),
        ),
        migrations.AlterField(
            model_name="article",
            name="view_count",
            field=models.PositiveIntegerField(
                default=0, verbose_name="количество просмотров"
            ),
        ),
    ]
