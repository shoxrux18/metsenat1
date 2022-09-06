from rest_framework import serializers
from .models import Student

class StudentRegisterSerializer(serializers.ModelSerializer):
    passport = serializers.FileField(source='user.passport', read_only=True)
    class Meta:
        model = Student
        exclude = ("user",)