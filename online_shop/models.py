from autoslug import AutoSlugField
from django.db import models
from django.utils.text import slugify


class Product(models.Model):
    title = models.CharField(verbose_name="Название продукта",max_length=100)
    price = models.DecimalField(verbose_name="Цена", max_digits=5, decimal_places=2)
    description = models.TextField(verbose_name="Описание", max_length=500)
    category = models.ForeignKey('Category', related_name='category', verbose_name="Категория", on_delete=models.PROTECT)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['title']


class Category(models.Model):
    title = models.CharField(verbose_name="Название категории", max_length=100, db_index=True)
    slug = AutoSlugField(populate_from='title', unique=True, slugify=slugify)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']