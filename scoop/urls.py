from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('contact', views.contact, name="contact"),
    path('create', views.sale_create, name="create"),
    path('collections', views.collections, name="collections"),
    path('collection_detail/<int:pk>/', views.collection_detail, name='collection_detail'),
    path('collection_detail/<pk>/delete/', views.sale_delete, name="sale_delete"),
    path('collection_detail/<pk>/update/', views.sale_update, name="sale_update"),
    path('product/<int:pk>/', views.productview, name='productview'),
]