#messaging/urls.py
from django.urls import path
from .views import send_message, ConversationView

urlpatterns = [
    path('send/<int:receiver_id>/', send_message, name='send_message'),
    path('conversation/', ConversationView.as_view(), name='inbox'),
]
