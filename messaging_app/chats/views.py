# messaging_app/chats/views.py
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from .models import Message, Conversation
from .serializers import MessageSerializer, ConversationSerializer
from .permissions import IsParticipantOfConversation
from rest_framework import HTTP_403_FORBIDDEN

class MessageViewSet(viewsets.ModelViewSet):
    """
    Viewset for creating, reading, updating, and deleting messages.
    Only participants of the conversation can interact with the messages.
    """
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated, IsParticipantOfConversation]

    def get_queryset(self):
        """
        Only allow the user to access messages from conversations they are a participant in.
        """
        conversation_id = self.kwargs.get('conversation_id')  # Get conversation ID from URL
        if conversation_id:
            return Message.objects.filter(conversation_id=conversation_id, conversation__participants=self.request.user)
        return Message.objects.none()

    def perform_create(self, serializer):
        """
        Ensure the user is a participant in the conversation when creating a message.
        """
        conversation = serializer.validated_data['conversation']
        if self.request.user not in conversation.participants.all():
            raise PermissionDenied("You are not a participant of this conversation.")
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        """
        Ensure the user is a participant in the conversation before updating a message.
        """
        message = self.get_object()
        conversation = message.conversation
        if self.request.user not in conversation.participants.all():
            raise PermissionDenied("You are not a participant of this conversation.")
        serializer.save()

    def perform_destroy(self, instance):
        """
        Ensure the user is a participant in the conversation before deleting a message.
        """
        conversation = instance.conversation
        if self.request.user not in conversation.participants.all():
            raise PermissionDenied("You are not a participant of this conversation.")
        instance.delete()

class ConversationViewSet(viewsets.ModelViewSet):
    """
    Viewset for managing conversations. Only participants can view or manage a conversation.
    """
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer
    permission_classes = [IsAuthenticated, IsParticipantOfConversation]

    def get_queryset(self):
        """
        Only allow the user to access conversations they are a participant in.
        """
        return Conversation.objects.filter(participants=self.request.user)
