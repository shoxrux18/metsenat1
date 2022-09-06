from .serializers import StudentRegisterSerializer
from .models import Student
from rest_framework import generics
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser

class StudentRegisterView(generics.CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentRegisterSerializer
    parser_classes = (MultiPartParser, FormParser, JSONParser)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)