from rest_framework import serializers

from .models import Customer, CustomerAddress

class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Customer
        fields = ('firstName', 'lastName', 'dob')

class CustomerAddressSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CustomerAddress
        fields = ('user','street_address', 'city', 'postal_code', 'country')