from rest_framework import viewsets, status, filters
from rest_framework.response import Response
from .models import Conversation, Message
from .serializers import ConversationSerializer, MessageSerializer


class ConversationViewSet(viewsets.ModelViewSet):
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['participants__first_name', 'participants__last_name']

    def perform_create(self, serializer):
        conversation = serializer.save()
        conversation.participants.add(self.request.user)
        conversation.save()


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['message_body']

    def perform_create(self, serializer):
        serializer.save(sender=self.request.user)
