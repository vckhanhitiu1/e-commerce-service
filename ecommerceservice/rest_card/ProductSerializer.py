from rest_framework import serializers
from .models import Product
class ProductSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=120)
    price = serializers.IntegerField()
    description = serializers.CharField()

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        return Product.objects.create(**validated_data)

    class Meta:
        model = Product
        fields = ('id', 'title', 'price', 'description')


