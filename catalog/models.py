from django.db import models

NULLABLE = {"blank": True, "null": True}


class Category(models.Model):
    """
    Класс категории товара
    """

    name = models.CharField(
        max_length=100,
        verbose_name="Наименование",
        help_text="Введите наименование категории",
    )

    description = models.TextField(
        verbose_name="Описание",
        help_text="Введите описание категории",
        **NULLABLE,
    )

    def __str__(self):
        """
        Строковое категории
        """
        return f"{self.name}"

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"
        ordering = ("name",)


class Product(models.Model):
    """
    Класс товара
    """

    name = models.CharField(
        max_length=100,
        verbose_name="Товар",
        help_text="Введите наименование товара",
    )

    description = models.TextField(
        verbose_name="Описание",
        help_text="Введите описание товара",
        **NULLABLE,
    )

    preview = models.ImageField(
        upload_to="preview",
        verbose_name="Изображение",
        help_text="Загрузите изображение товара",
        **NULLABLE,
    )

    category = models.ForeignKey(
        "Category",
        on_delete=models.SET_NULL,
        verbose_name="Категория",
        help_text="Введите категорию товара",
        related_name="products",
        **NULLABLE,
    )

    price = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        verbose_name="Цена",
        help_text="Введите цену",
        default=0.0,
    )

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name="Дата последнего изменения"
    )

    manufactured_at = models.DateTimeField(**NULLABLE, verbose_name="Дата производства продукта")

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "товар"
        verbose_name_plural = "товары"
        ordering = (
            "name",
            "price",
            "created_at",
            "updated_at",
            "category",
        )
