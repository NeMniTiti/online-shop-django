from django.apps import AppConfig


class OnlineShopConfig(AppConfig):
    verbose_name = 'Shop'
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'online_shop'

    def ready(self):
        import online_shop.signals