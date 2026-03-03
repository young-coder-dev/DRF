from django.shortcuts import render,get_object_or_404
from .serializers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.db.models import Max
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from django.shortcuts import redirect
# Create your views here.

class ProductListAPIView(generics.ListAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    permission_classes=[IsAuthenticated]

    def get_queryset(self):
        qs=super().get_queryset()
        return qs.filter(price__lt=20)

# @api_view(["GET"])
# def product_list(request):
#     products=Product.objects.all()
#     serializer=ProductSerializer(products,many=True)
#     return Response(serializer.data)


class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    lookup_url_kwarg='pk'

# @api_view(['GET'])
# def product_detail(request, pk):
#     product = get_object_or_404(Product, pk=pk)
#     serializer = ProductSerializer(product)
#     return Response(serializer.data)


class OrderListAPIView(generics.ListAPIView):
    queryset=Order.objects.prefetch_related('items__product')
    serializer_class=OrderSerializer

# @api_view(['GET'])
# def order_list(request):
#     orders = Order.objects.prefetch_related('items__product')
#     serializer = OrderSerializer(orders, many=True)
#     return Response(serializer.data)
class ProductInfoAPIView(APIView):
    def get(self,request):
        products=Product.objects.all()
        serializers=ProductInfoSerializer({
            'products':products,
            'count':len(products),
            'max_price':products.aggregate(max_price=Max('price'))['max_price']
        })
        return Response(serializers.data)

# @api_view(['GET'])
# def product_info(request):
#     products = Product.objects.all()
#     serializer = ProductInfoSerializer({
#         'products': products,
#         'count': len(products),
#         'max_price': products.aggregate(max_price=Max('price'))['max_price']
#     })
#     return Response(serializer.data)

# class ProductCreateAPIView(generics.CreateAPIView):
class ProductCreateAPIView(generics.ListCreateAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductCreateSerializer
    def create(self, request, *args, **kwargs):
        response=super().create(request, *args, **kwargs)
        return redirect('create')