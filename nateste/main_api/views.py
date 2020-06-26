from rest_framework.response import Response

from .models import Order , User
from .serializers import OrderSerializer , UserSerializer
from rest_framework import generics, viewsets


class OrderList(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer



class CreateUser(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# class UpdateUser(generics.RetrieveUpdateDestroyAPIView):
#     queryset =
