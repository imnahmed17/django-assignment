from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('get_product_name_suggestions/', views.get_product_name_suggestions, name='get_product_name_suggestions'),
    path('<int:product_id>/', views.product_details, name='product_details'),
    path('<int:product_id>/add_review/', views.add_review, name='add_review'),
]