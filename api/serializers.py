from rest_framework import serializers
from .models import Student

class StudentRegisterSerializer(serializers.ModelSerializer):
    passport = serializers.FileField(source='user.passport', read_only=True)
    class Meta:
        model = Student
<<<<<<< HEAD
        exclude = ("user",)
=======
        exclude = ("user",)



class StudentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('first_name', 'last_name', 'university', 'price', 'passport')

>>>>>>> b4f84d110abac91e3e728c058c03343c18dccad5
