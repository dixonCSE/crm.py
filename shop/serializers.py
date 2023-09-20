from .models import Product
from django.contrib.auth.models import User
from rest_framework import serializers


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'image']

 
 
class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields =  '__all__'