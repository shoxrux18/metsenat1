from .serializers import StudentRegisterSerializer, StudentListSerializer
from .models import Student, Sponsor
from rest_framework import generics
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework.response import Response
from .filter import FilterStudent
from rest_framework.permissions import IsAuthenticated,AllowAny


class StudentRegisterView(generics.CreateAPIView):
    permission_classes = [AllowAny]
    queryset = Student.objects.all()
    serializer_class = StudentRegisterSerializer
    parser_classes = (MultiPartParser, FormParser, JSONParser)

    def perform_create(self, serializer):

        serializer.save(user=self.request.user)

        


class StudentListView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Student.objects.all()
    serializer_class = StudentListSerializer




class StudentListViews(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Student.objects.all()
    serializer_class = StudentListSerializer
   

    def get_queryset(self):
        user = self.request.user.is_authenticated
        if user:
            univer = self.kwargs['pk']
            student = Student.objects.filter(university_id=univer).all()
            return student
        return Response(data={
            "user_id": "you need register"
        })


