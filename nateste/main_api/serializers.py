from .models import Review, Order
from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username',  # 'profile.created_at', 'profile.updated_at',
                  'first_name', 'last_name',  # 'profile.is_cooker', 'profile.bio', 'profile.rating',
                  'email']




class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'title', "deadline", 'description', 'is_active', 'weight', 'price', 'created_at', 'updated_at',
                  'customer', 'worker']


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'title', 'description', 'updated_at',
                  'created_at', 'rating', 'customer', 'worker']

# from main_api.serializers import OrderSerializer
# ser = OrderSerializer()
# print (ser)
