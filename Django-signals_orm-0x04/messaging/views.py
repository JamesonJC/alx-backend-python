# messaging/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.generic import ListView
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.contrib.auth import logout
from messaging.models import Message

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
        return redirect('inbox')  # Adjust as needed

    return render(request, 'messaging/send_message.html', {'receiver_id': receiver_id})

@method_decorator(cache_page(60), name='dispatch')
class ConversationView(ListView):
    model = Message
    template_name = 'messaging/conversation.html'
    context_object_name = 'messages'

    def get_queryset(self):
        return Message.objects.filter(
            receiver=self.request.user
        ).sele
#["user.delete()", "delete_user"]ct_related('sender').order_by('-timestamp') ["select_related"]


@method_decorator(cache_page(60), name='dispatch')
class MessageListView(ListView):
    model = Message
    template_name = 'chat/message_list.html'
    context_object_name = 'messages'

    def get_queryset(self):
        user = self.request.user
        return Message.objects.filter(receiver=user).select_related('sender')