from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Message
from .serializers import MessageSerializer

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all().order_by('-created_at')
    serializer_class = MessageSerializer
    filterset_fields = ['status', 'type']

    @action(detail=True, methods=['post'])
    def mark_as_sent(self, request, pk=None):

        message = self.get_object()

        message.status = 'sent'
        message.save()

        serializer = self.get_serializer(message)
        return Response(serializer.data)