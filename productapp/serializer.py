from rest_framework import serializers
from .models import ProductModel,ComapanyModel


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = ComapanyModel
        fields = '__all__'
        


class ProductSerializer(serializers.ModelSerializer):
    company = CompanySerializer()
    class Meta:
        model = ProductModel
        fields = '__all__'

