from rest_framework import serializers
from api.models import Student



class PaymentSerializer(serializers.Serializer):
    student = serializers.PrimaryKeyRelatedField(queryset=Student.objects.all())
    amount = serializers.DecimalField(max_digits=8, decimal_places=2)

    def validate_amount(self, amount):
        user = self.context['request'].user
        if user.sponsor.price < amount:
            raise serializers.ValidationError('Not enough money')
        return amount