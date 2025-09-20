
from django.db.models.signals import post_save, post_delete
from django.core.cache import cache
from django.dispatch import receiver

from .models import Product, Category


class A:
    print('Я вызвался!!  '*10)

print(A())


@receiver([post_save, post_delete], sender=Product)
def clear_product_cache(sender, instance, **kwargs):
    cache.delete('list_products')
    if instance.category:
        cache.delete(f'product_{instance.category.pk}')


@receiver([post_save, post_delete], sender=Category)
def clear_category_cache(sender, instance, **kwargs):
    cache.delete('list_categories')
    if instance.category:
        cache.delete('list_products')