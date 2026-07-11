from django.urls import path
from . import views

# This name lets the form use shop:shop in the template.
app_name = "shop"

# This url sends the shop link to the shop view.
urlpatterns = [
    path('shop/', views.shop, name='shop'),
    path('shop/manage/', views.manage_products, name='manage_products'),
    path('shop/add/', views.add_product, name='add_product'),
    path('shop/add-category/', views.add_category, name='add_category'),
    path('shop/add-sub-category/', views.add_sub_category, name='add_sub_category'),
    path('shop/edit-product/', views.edit_product, name='edit_product'),
    path('shop/delete-product/', views.delete_product, name='delete_product'),
    path('shop/delete-category/', views.delete_category, name='delete_category'),
    path('shop/delete-sub-category/', views.delete_sub_category, name='delete_sub_category'),
    path('shop/category/', views.category_page, name='category_page'),
    path('shop/Rods', views.rods, name='rods'),
    path('shop/Reels', views.reels, name='reels'),
    path('shop/Lines', views.lines, name='lines'),
    path('shop/Lures', views.lures, name='lures'),
    path('shop/Accessories', views.accessories, name='accessories'),
]
