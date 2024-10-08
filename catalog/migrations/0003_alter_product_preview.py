# Generated by Django 5.1.1 on 2024-09-26 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0002_contact"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="preview",
            field=models.ImageField(
                blank=True,
                help_text="Загрузите изображение товара",
                null=True,
                upload_to="blog/preview",
                verbose_name="Изображение",
            ),
        ),
    ]
