from django.urls import path
from . import views

# This name lets the form use shop:shop in the template.
app_name = "shop"

# This url sends the shop link to the shop view.
urlpatterns = [
    path('shop/', views.shop, name='shop'),
    path('shop/manage/', views.manage_products, name='manage_products'),
    path('shop/add/', views.add_product, name='add_product'),
    path('shop/edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path('shop/delete/<int:product_id>/', views.delete_product, name='delete_product'),
    path('shop/Rods', views.rods, name='rods'),
    path('shop/Rods/', views.rods),
    path('shop/Reels', views.reels, name='reels'),
    path('shop/Reels/', views.reels),
    path('shop/Lines', views.lines, name='lines'),
    path('shop/Lines/', views.lines),
    path('shop/Lures', views.lures, name='lures'),
    path('shop/Lures/', views.lures),
    path('shop/Accessories', views.accessories, name='accessories'),
    path('shop/Accessories/', views.accessories),
]
