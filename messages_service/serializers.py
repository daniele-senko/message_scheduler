from rest_framework import serializers
from django.utils import timezone
from .models import Message

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id', 'type', 'content', 'scheduled_at', 'status', 'created_at']
    
    def validate_scheduled_at(self, value):
        # value é a data que o usuário está tentando enviar
        if value < timezone.now():
            raise serializers.ValidationError("O agendamento não pode ser no passado.")
        return value