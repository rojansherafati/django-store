from django.contrib import admin
from django.urls import path
from . import views
urlpatterns=[
    path('index/',views.index),
    path('customers/get/all/',views.customers_get_all),
    path('customers/delete/<int:id>/',views.customers_delete),
    path('customers/edit/<int:id>/',views.customers_edit),
    path('customers/store/',views.customers_store),
    path('customers/',views.customers_index),

    path('sellers/get/all/',views.sellers_get_all),
    path('sellers/delete/<int:id>/',views.sellers_delete),
    path('sellers/edit/<int:id>/',views.sellers_edit),
    path('sellers/store/',views.sellers_store),
    path('sellers/',views.sellers_index),

    path('products/get/one/',views.products_get_one),
    path('products/get/all/',views.products_get_all),
    path('products/delete/<int:id>/',views.products_delete),
    path('products/edit/<int:id>/',views.products_edit),
    path('products/store/',views.products_store),
    path('products/form/',views.products_form),
    path('products/',views.products_index),

    path('categories/get/all/',views.categories_get_all),
    path('categories/edit/<int:id>/',views.categories_edit),
    path('categories/get/data/',views.categories_get_data),
    path('categories/delete/<int:id>/',views.categories_delete),
    path('categories/modal/store/',views.categories_modal_store),
    path('categories/store/',views.categories_store),
    path('categories/',views.categories_index),

    path('brands/get/all/',views.brands_get_all),
    path('brands/edit/<int:id>/',views.brands_edit),
    path('brands/get/data/',views.brands_get_data),
    path('brands/delete/<int:id>/',views.brands_delete),
    path('brands/modal/store/',views.brands_modal_store),
    path('brands/store/',views.brands_store),
    path('brands/',views.brands_index),

]