# messaging_app/chats/views.py
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Message, Conversation
from .serializers import MessageSerializer, ConversationSerializer
from .permissions import IsParticipantOfConversation

class MessageViewSet(viewsets.ModelViewSet):
    """
    Viewset for creating, reading, updating, and deleting messages.
    Only participants of the conversation can interact with the messages.
    """
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated, IsParticipantOfConversation]

    def get_queryset(self):
        # Ensure that users can only see messages from conversations they're part of
        return Message.objects.filter(conversation__participants=self.request.user)

    def perform_create(self, serializer):
        # Ensure that the user is a participant in the conversation when creating a new message
        conversation = serializer.validated_data['conversation']
        if self.request.user not in conversation.participants.all():
            raise PermissionError("You are not a participant of this conversation.")
        serializer.save(user=self.request.user)

class ConversationViewSet(viewsets.ModelViewSet):
    """
    Viewset for managing conversations. Only participants can view or manage a conversation.
    """
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer
    permission_classes = [IsAuthenticated, IsParticipantOfConversation]

    def get_queryset(self):
        # Ensure that users can only see conversations they're part of
        return Conversation.objects.filter(participants=self.request.user)
