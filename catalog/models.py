from django.db import models


class Category(models.Model):
    """
    Класс категории товара
    """

    name = models.CharField(
        max_length=100,
        verbose_name="Наименование",
        help_text="Введите наименование категории",
    )

    def __str__(self):
        """
        Строковое категории
        """
        return f"{self.name}"

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"


class Product(models.Model):
    """
    Класс товара
    """

    name = models.CharField(
        max_length=100,
        verbose_name="Товар",
        help_text="Введите наименование товара",
    )

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "товар"
        verbose_name_plural = "товары"
