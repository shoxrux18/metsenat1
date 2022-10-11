from rest_framework import serializers
from account.models import User
from api.models import Student,Sponsor
from django.db import models



class PaymentSerializer(serializers.Serializer):
    user = serializers.CharField(source='student.id')
    first_name = serializers.CharField(max_length=255)
    university = serializers.CharField(source='student.university.id')
    price = serializers.DecimalField(write_only=True,max_digits=8, decimal_places=2)

    
          
    def create(self, validated_data):
        return Student(**validated_data)