# messaging_app/chats/permissions.py
from rest_framework import permissions
from .models import Conversation, Message

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow users to view or edit their own messages.
    """

    def has_object_permission(self, request, view, obj):
        # Check if the request is read-only or if the user is the owner of the object
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user  # Assuming `user` is a field on your message model

class IsParticipantOfConversation(permissions.BasePermission):
    """
    Custom permission to only allow participants in a conversation to send, view, update, or delete messages.
    """

    def has_permission(self, request, view):
        """
        This method will be used for the general permission checks for the view.
        Here we check if the user is authenticated.
        """
        # Ensure the user is authenticated
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        """
        This method will be used for the object-level permission checks.
        Here we check if the user is a participant in the conversation related to the message.
        """
        # If the object is a message, check if the user is part of the conversation
        if isinstance(obj, Message):
            conversation = obj.conversation  # Assuming each message has a related conversation
            return conversation.participants.filter(id=request.user.id).exists()  # Check if the user is in the conversation

        return False