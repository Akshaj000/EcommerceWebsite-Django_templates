from rest_framework import serializers
from ecom.models import*

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Customer
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields = '__all__'

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model=Cart
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model=Order
        fields = '__all__'