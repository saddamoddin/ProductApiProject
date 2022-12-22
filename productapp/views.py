from django.shortcuts import render
from .serializer import ProductSerializer , CompanySerializer
from .models import ProductModel , ComapanyModel
from rest_framework.viewsets import ModelViewSet
# Create your views here.

class ProductView(ModelViewSet):
    queryset = ProductModel.objects.all().order_by('-price')
    serializer_class = ProductSerializer

    

class CompanyView(ModelViewSet):
    queryset = ComapanyModel.objects.all()
    serializer_class = CompanySerializer
