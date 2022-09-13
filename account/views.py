from .models import User
from .serializers import RegisterSerializer
from rest_framework import generics
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser,FileUploadParser
from rest_framework.permissions import AllowAny
from rest_framework.response import Response


class RegisterView(generics.CreateAPIView):    
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]
    
    
    
