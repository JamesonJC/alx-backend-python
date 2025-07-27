# messaging_app/chats/filters.py
import django_filters
from .models import Message

class MessageFilter(django_filters.FilterSet):
    """
    Filter for retrieving messages based on user or date range.
    """
    user = django_filters.CharFilter(field_name="user__username", lookup_expr='icontains', label='User')
    start_date = django_filters.DateTimeFilter(field_name="created_at", lookup_expr='gte', label='Start Date')
    end_date = django_filters.DateTimeFilter(field_name="created_at", lookup_expr='lte', label='End Date')

    class Meta:
        model = Message
        fields = ['user', 'start_date', 'end_date']
