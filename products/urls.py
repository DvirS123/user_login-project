from django.contrib import admin
from django.urls import path , include
from . import views
from .models import Product

urlpatterns = [
	path('create/', views.create, name = 'create'),
	path('all_products/', views.all_products, name = 'all_products'),
	path('<int:product_id>/', views.products_detail, name='product_detail'),
	]