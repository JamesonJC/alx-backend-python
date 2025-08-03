# messaging_app/chats/auth.py
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework.exceptions import AuthenticationFailed

def get_user_from_jwt(token):
    """
    Given a JWT token, return the user associated with the token.
    """
    try:
        # Decode and validate the token
        access_token = AccessToken(token)
        user_id = access_token['user_id']
        return User.objects.get(id=user_id)  # Assuming User is your user model
    except Exception as e:
        raise AuthenticationFailed('Invalid token')
