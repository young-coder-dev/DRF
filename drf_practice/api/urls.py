from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list),
    path('info/', views.product_info),
    path('<int:pk>/', views.product_detail),
    path('orders/', views.order_list),
]