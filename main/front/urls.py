from django.urls import path
from . import views


app_name = 'front'


urlpatterns = [
    path('', views.index, name='index'),
    path('product/<str:code>', views.product_detail, name='product_detail'),
    path('category/<str:code>', views.product_list, name='product_list'),
    path('carts', views.carts, name='carts'),
    path('cart/<str:code>/', views.cart_detail, name='cart_detail'),
    path('active/cart', views.active_cart, name='active_cart'),

]