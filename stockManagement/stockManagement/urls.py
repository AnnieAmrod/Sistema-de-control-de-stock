"""stockManagement URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from stockManagementApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', views.HomeView.as_view(), name='home'),
    path('', views.home_view, name='home'),
    path('list_items/', views.list_items_view, name='list_items'),
    path('add_items/', views.add_items_view, name='add_items'),
    path('update_items/<str:pk>/', views.update_items_view, name='update_items'),
    path('delete_items/<str:pk>/', views.delete_items_view, name='delete_items'),
    path('list_categories/', views.list_categories_view, name='list_categories'),
    path('add_categories/', views.add_categories_view, name='add_categories'),
    path('update_categories/<str:pk>/', views.update_categories_view, name='update_categories'),
    path('delete_categories/<str:pk>/', views.delete_categories_view, name='delete_categories'),
    path('item_detail/<str:pk>/', views.item_detail_view, name='item_detail'),
    path('items_gastados/<str:pk>/', views.items_gastados_view, name='items_gastados'),
    path('items_comprados/<str:pk>/', views.items_comprados_view, name='items_comprados'),
]
