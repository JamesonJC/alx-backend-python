# messaging_app/chats/permissions.py
from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow users to view or edit their own messages.
    """

    def has_object_permission(self, request, view, obj):
        # Check if the request is read-only or if the user is the owner of the object
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user  # Assuming `user` is a field on your message model
