from rest_framework import generics
from rest_framework.views import APIView
from .serializers import PaymentSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,AllowAny
from account.models import User
from api.models import Sponsor, Student
from api import permissons

class PaymentView(APIView):
    permission_classes = [permissons.IsSponsor]
    def post(self,request):
        serializer = PaymentSerializer(data=request.data)
        if serializer.is_valid():
            price_sum = serializer.validated_data.get('price')
            student = serializer.validated_data.get('user')
            sponsor = Sponsor.objects.get(user=request.user)
            user1 = Student.objects.get(id=student)
            sponsor.price -= price_sum
            user1.price += price_sum
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

        
    




    
