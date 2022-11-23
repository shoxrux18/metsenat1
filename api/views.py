from django.shortcuts import get_object_or_404
from .serializers import StudentRegisterSerializer, StudentListSerializer,SponsorRegisterSerializer
from .models import Student, University
from rest_framework import generics
from rest_framework import permissions
from . import permissons as api_permissons
from rest_framework.views import APIView
from rest_framework.response import Response

class StudentRegisterView(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated,]
    serializer_class = StudentRegisterSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        

class SponsorRegisterView(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated,]
    serializer_class = SponsorRegisterSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class StudentListView(generics.ListAPIView):
    permission_classes = [api_permissons.IsSponsor,]
    queryset = Student.objects.select_related('university')
    serializer_class = StudentListSerializer


class UniversityStudentsView(APIView):
    permission_classes = [api_permissons.IsSponsor,]
    
    def get(self, request, pk):
        university = get_object_or_404(University, pk=pk)
        students = university.student_set.all()
        serializer = StudentListSerializer(students, many=True)
        return Response(serializer.data)