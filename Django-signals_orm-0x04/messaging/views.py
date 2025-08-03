# messaging/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.generic import ListView
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

from .models import Message


@login_required
def send_message(request, receiver_id):
    if request.method == 'POST':
        content = request.POST.get('content')
        receiver = get_object_or_404(User, id=receiver_id)

        Message.objects.create(
            sender=request.user,
            receiver=receiver,
            content=content
        )
        return redirect('inbox')

    return render(request, 'messaging/send_message.html', {'receiver_id': receiver_id})


@method_decorator(cache_page(60), name='dispatch')
class ConversationView(ListView):
    model = Message
    template_name = 'messaging/conversation.html' 
    context_object_name = 'messages'

    def get_queryset(self):
        # Get all messages sent to the logged-in user with related user data
        return Message.objects.filter(
            receiver=self.request.user
        ).select_related('sender', 'receiver').order_by('-timestamp')
