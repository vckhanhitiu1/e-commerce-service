from rest_framework import serializers
from .models import Product
class ProductSerializer(serializers.Serializer):
    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass

    class Meta:
        model = Product


