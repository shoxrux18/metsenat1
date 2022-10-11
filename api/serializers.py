from rest_framework import serializers
from .models import Student,Sponsor,University

class StudentRegisterSerializer(serializers.ModelSerializer):
    passport = serializers.FileField(read_only=False)
    class Meta:
        model = Student
        exclude = ("user",)



class SponsorRegisterSerializer(serializers.ModelSerializer):
    passport = serializers.FileField(read_only=False)
    class Meta:
        model = Sponsor
        exclude = ("user",)



class StudentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('first_name', 'last_name', 'university', 'price', 'passport')


class SponsorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sponsor
        fields = ('first_name', 'last_name', 'passport','price')