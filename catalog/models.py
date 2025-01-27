from django.db import models
from django.core.validators import MaxValueValidator

from users.models import User


class Product(models.Model):
    """содержит поля наименование, описание, изображение, категория, цена за покупку,дата создания,дата последнего изменения."""
    name = models.CharField(
        max_length=100,
        verbose_name="Название продукта",
        help_text="Введите название продукта",
    )
    description = models.TextField(
        verbose_name="Описание продукта", help_text="Введите описание продукта"
    )
    image = models.ImageField(
        upload_to="catalog/image",
        blank=True,
        null=True,
        verbose_name="Фото продукта",
        help_text="Загрзите фото продукта",
    )
    category = models.CharField(
        max_length=100, verbose_name="Категория", help_text="Введите категорию"
    )
    price = models.IntegerField(
        default=0, validators=[MaxValueValidator(1000000)], verbose_name="Цена за продукт"
    )
    created_at = models.DateField(
        blank=True,
        null=True,
        verbose_name="Дата создания",
        help_text="Введите дату создания",
    )
    updated_at = models.DateField(
        blank=True,
        null=True,
        verbose_name="дата последнего изменения",
        help_text="Введите дату последнего изменения",
    )
    views_counter = models.PositiveIntegerField(
        verbose_name="Счетчик просмотров",
        help_text="Укажите кол-во просмотров",
        default=0
    )
    owner = models.ForeignKey(User, verbose_name='Владелец', help_text='Укажите владельца собаки', blank=True,
                              null=True,
                              on_delete=models.SET_NULL)

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["name", "category"]
        permissions = [
            ('can_edit_product', 'can edit product'),
            ('can_edit_descriptions', 'can edit descriptions'),
        ]

    def __str__(self):
        return self.name


class Category(models.Model):
    """содержит поля наименование,описание."""

    name = models.CharField(
        max_length=100,
        verbose_name="Название категории",
        help_text="Введите название категории",
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name="Описание категории",
        help_text="Введите описание категории"
    )

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name
