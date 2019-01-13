from django.shortcuts import render

# Create your views here.
from rest_framework.generics import (
    ListCreateAPIView,
    )
from rest_framework import viewsets
from rest_framework import serializers
# from .models import Post


# class PostListSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Post
#         fields = '__all__'
#
#
#
# class PostListCreateAPIView(viewsets.GenericViewSet,
#                             ListCreateAPIView):
#     serializer_class = PostListSerializer
#     queryset = Post.objects.all()