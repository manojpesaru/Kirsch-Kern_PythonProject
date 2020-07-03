from django.shortcuts import render
from rest_framework import viewsets

from .serializers import CustomerSerializer, CustomerAddressSerializer
from .models import Customer,CustomerAddress


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all().order_by('lastName')
    serializer_class = CustomerSerializer

class CustomerAddressViewSet(viewsets.ModelViewSet):
    queryset = CustomerAddress.objects.all()
    serializer_class = CustomerAddressSerializer