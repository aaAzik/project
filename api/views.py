from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.status import *
from drf_spectacular.utils import extend_schema
from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.permissions import IsAdminUser
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import ProductSerializers
from scoop.models import Product

class ProductViewSet(ViewSet):
    @extend_schema(responses=ProductSerializers(many=True))
    def list(self, request):
        product = Product.objects.all()
        serializer = ProductSerializers(product, many=True)
        return Response(serializer.data, status=200)
    
    @extend_schema(request=ProductSerializers(), responses=ProductSerializers())
    def create(self, request):
        serializer = ProductSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
    @extend_schema(request=ProductSerializers(), responses=ProductSerializers())
    def retrive(self, request, pk=None):
        product = Product.objects.get(pk=pk)
        serializer = ProductSerializers(product)
        return Response(serializer.data, status=200)
    
    @extend_schema(request=ProductSerializers(), responses=ProductSerializers())
    def partial_update(self, request, pk=None):
        product = Product.objects.get(pk=pk)
        serializer = ProductSerializers(product, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
    @extend_schema(responses=None)
    def destroy(self, request, pk=None):
        product = Product.objects.get(pk=pk)
        product.delete()
        return Response('DELETED', status=204)