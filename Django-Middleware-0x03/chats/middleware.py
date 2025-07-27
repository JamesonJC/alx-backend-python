# Django-Middleware-0x03/chats/middleware.py
import logging
from datetime import datetime
from django.http import HttpResponseForbidden
from collections import defaultdict
from django.http import HttpResponseForbidden

# Create a logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler('requests.log')
formatter = logging.Formatter('%(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

class RequestLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Get user info
        user = request.user if request.user.is_authenticated else "Anonymous"
        # Log the request data
        logger.info(f"{datetime.now()} - User: {user} - Path: {request.path}")
        
        # Proceed with the request
        response = self.get_response(request)
        return response

class RestrictAccessByTimeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        current_hour = datetime.now().hour

        # If the current time is not between 9 PM and 6 AM, deny access
        if current_hour < 6 or current_hour >= 21:
            return HttpResponseForbidden("Access Denied: The chat is only available between 9 AM and 9 PM.")
        
        # Proceed with the request if the time is valid
        response = self.get_response(request)
        return response

class OffensiveLanguageMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # Dictionary to store message counts per IP
        self.message_counts = defaultdict(list)

    def __call__(self, request):
        if request.method == 'POST' and request.path.startswith('/api/conversations/'):
            ip_address = request.META.get('REMOTE_ADDR')
            current_time = datetime.now()

            # Clean up messages older than 1 minute
            self.message_counts[ip_address] = [timestamp for timestamp in self.message_counts[ip_address] if (current_time - timestamp).seconds < 60]

            # If the number of messages in the last minute exceeds the limit (5), block the request
            if len(self.message_counts[ip_address]) >= 5:
                return HttpResponseForbidden("You have exceeded the limit of 5 messages per minute.")
            
            # Add current message's timestamp
            self.message_counts[ip_address].append(current_time)
        
        response = self.get_response(request)
        return response

from django.http import HttpResponseForbidden

class RolepermissionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Check if the user is authenticated and has the required role
        if request.user.is_authenticated:
            if not (request.user.role == 'admin' or request.user.role == 'moderator'):
                return HttpResponseForbidden("You do not have permission to access this resource.")
        
        # Proceed with the request
        response = self.get_response(request)
        return response
