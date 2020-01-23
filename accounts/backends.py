from django.contrib.auth.models import User

class EmailAuth:
    """Authenticate a user by an exact match on the email and password"""
    def authenticate(self, username=None, password=None):               # Say that username and password are None by default.
        """
        Get an instance of `User` based off the email and verify the
        password
        """
        try:
            user = User.objects.get(email=username)                     # The reason this is called username here is because that's what the name of the the form element is. 
            if user.check_password(password):                           # If password validation is good: return user, otherwise: return none.
                return user
            return None
        except User.DoesNotExist:
            return None
    
    def get_user(self, user_id):
        """
        Used by the Django authentiation system to retrieve a user instance
        """     
        try:
            user = User.objects.get(pk=user_id)

            if user.is_active:                                      # if it's an active user: return that user. Otherwise: return none and then another except block will do the same as above
                return user
            return None
        except User.DoesNotExist:
            return None