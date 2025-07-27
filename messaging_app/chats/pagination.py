# messaging_app/chats/pagination.py
from rest_framework.pagination import PageNumberPagination

class MessagePagination(PageNumberPagination):
    """
    Custom pagination class for messages. 
    It will return 20 messages per page by default.
    """
    page_size = 20  # Set the default number of messages per page
    page_size_query_param = 'page_size'  # Allow clients to specify the page size
    max_page_size = 100  # Limit the maximum page size to 100
