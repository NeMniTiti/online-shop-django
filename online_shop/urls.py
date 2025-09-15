
from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.get_list_products, name='get_list_products'),
    path('category/', views.get_list_categories, name='get_list_categories'),
    path('category/<str:slug>/', views.get_category_detail, name='get_category_detail'),
    path('product/<int:pk>/', views.get_product_detail, name='get_product_detail'),
    path('add_category/', views.add_category, name='add_category'),
    path('add_product/', views.add_product, name='add_product'),
]