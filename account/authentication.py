from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

class CustomAuthenticationBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        print(request)
        UserModel = get_user_model()
        
        try:
            # Vérifiez si l'utilisateur est un admin
            if '@' in username:  # Si c'est un email
                user = UserModel.objects.get(email=username)
            else:  # Sinon, il s'agit d'un matricule
                user = UserModel.objects.get(matricule=username)
        except UserModel.DoesNotExist:
            return None

        if user.check_password(password):
            return user
        return None