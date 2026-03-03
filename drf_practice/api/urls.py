from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProductListAPIView.as_view(),name='products'),
    path('info/', views.product_info),
    path('<int:pk>/', views.ProductDetailAPIView.as_view()),
    path('orders/', views.OrderListAPIView.as_view(),name='user-orders'),
]