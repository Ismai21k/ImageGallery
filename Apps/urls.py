from django.urls import path
from . import views




urlpatterns = [
    path('', views.product, name='product'),
    path('add/', views.add_product, name='add_product'),
    path('edit/<int:pk>/', views.product_edit, name='edit_product'),
    path('del/<int:pk>/', views.delete_product, name='delete_product'),
]