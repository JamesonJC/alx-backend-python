# messaging_app/chats/permissions.py
from rest_framework import permissions
from .models import Message

class IsParticipantOfConversation(permissions.BasePermission):
    """
    Custom permission to only allow participants in a conversation to send, view, update, or delete messages.
    """

    def has_permission(self, request, view):
        """
        This method checks if the user is authenticated.
        """
        # Ensure the user is authenticated
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        """
        This method checks if the user is a participant in the conversation related to the message.
        It handles various HTTP methods like GET, PUT, PATCH, DELETE.
        """
        # Get the conversation object from the message
        if isinstance(obj, Message):
            conversation = obj.conversation  # Assuming each message has a related conversation

            # Check if the user is a participant of the conversation
            is_participant = conversation.participants.filter(id=request.user.id).exists()

            # Allow only GET requests (viewing messages)
            if request.method in permissions.SAFE_METHODS:
                return is_participant

            # Allow PUT, PATCH, DELETE only if the user is a participant
            if request.method in ['PUT', 'PATCH', 'DELETE']:
                return is_participant

        return False
    