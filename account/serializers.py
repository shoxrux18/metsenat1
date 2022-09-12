from random import choices
from rest_framework.response import Response
from rest_framework import serializers
from .models import User
from phonenumber_field.serializerfields import PhoneNumberField
from rest_framework import exceptions, serializers, status

class RegisterSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=100, write_only=True)
    password = serializers.CharField(write_only=True)
    confirm = serializers.CharField(write_only=True)
    phone_number = PhoneNumberField(write_only=True)
    role = serializers.ChoiceField(choices=User.Roles.choices, write_only=True)

    def create(self, validated_data):

        if validated_data["password"] != validated_data["confirm"]:
                raise exceptions.ValidationError(
                    detail={
                        "password": "Passwords not match",
                        "confirm": "Passwords not match",
                    }
                )
        user = User.objects.create(
            username=validated_data['username'],
            password=validated_data['password'],
            phone_number=validated_data['phone_number'],
            role=validated_data['role']

        )
        if user.password is not None:
            user.set_password(user.password)
        user.save()
        return user

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['username'] = instance.username        
        representation['role'] = instance.role
        return representation

    class Meta:
        model = User
        fields = '__all__'