from rest_framework import generics
from .ProductSerializer import ProductSerializer
from .models import Product
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend


@api_view(['GET'])
def product_get_all(request):
    queryset = Product.objects.all()
    serializer = ProductSerializer(queryset, many=True)
    title = request.query_params.get('title')
    price = request.query_params.get('price')
    id = request.query_params.get('id')

    if title is not None:
        product = Product.objects.filter(title=title)
        serializer = ProductSerializer(product, many=True)
        return Response(serializer.data)
    if price is not None:
        product = Product.objects.filter(price=price)
        serializer = ProductSerializer(product, many=True)
        return Response(serializer.data)
    if id is not None:
        product = Product.objects.filter(id=id)
        serializer = ProductSerializer(product, many=True)
        return Response(serializer.data)
    return Response(serializer.data)

@api_view(['POST'])
def create_new_product(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class ProductView(generics.ListCreateAPIView):
    def get_queryset(self):
        queryset = Product.objects.filter(title=self.kwargs['title'])
        return queryset


