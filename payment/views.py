from rest_framework.views import APIView
from .serializers import PaymentSerializer
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from api import models as api_models
from api import permissons

class PaymentView(APIView):
    permission_classes = [permissons.IsSponsor]
    
    def post(self,request):
        serializer = PaymentSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        amount = serializer.validated_data.get('amount')
        student = serializer.validated_data.get('student')
        sponsor = request.user.sponsor
        sponsor.price -= amount
        student.price += amount
        sponsor.save()
        student.save()
        return Response(serializer.data, status=200)

        
    




    
