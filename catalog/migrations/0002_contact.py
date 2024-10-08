# Generated by Django 5.1.1 on 2024-09-19 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Contact",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100, verbose_name="Имя")),
                ("phone", models.CharField(max_length=12, verbose_name="Телефон")),
                (
                    "address",
                    models.CharField(
                        blank=True, max_length=255, null=True, verbose_name="Адрес"
                    ),
                ),
            ],
            options={
                "verbose_name": "контакт",
                "verbose_name_plural": "контакты",
                "ordering": ("name",),
            },
        ),
    ]
