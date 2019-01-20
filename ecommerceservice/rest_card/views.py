from rest_framework import generics
from .ProductSerializer import ProductSerializer
from .models import Product
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def product_get_all(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


class ProductView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

