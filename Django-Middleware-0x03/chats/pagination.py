# messaging_app/chats/pagination.py
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

class MessagePagination(PageNumberPagination):
    """
    Custom pagination class for messages.
    It will return 20 messages per page by default.
    """
    page_size = 20  # Default number of messages per page
    page_size_query_param = 'page_size'  # Allows clients to specify the page size
    max_page_size = 100  # Limit the max page size to 100

    def get_paginated_response(self, data):
        """
        Custom paginated response that includes the total count of objects.
        """
        return Response({
            'count': self.page.paginator.count,  # Total number of items available
            'next': self.get_next_link(),  # URL for next page of results
            'previous': self.get_previous_link(),  # URL for previous page of results
            'results': data  # The actual list of data on the current page
        })
