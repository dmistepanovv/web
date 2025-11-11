from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend

class EmailOrUsernameModelBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        UserModel = get_user_model()
        try:
            # Пытаемся найти пользователя по email
            user = UserModel.objects.get(email=username)
        except UserModel.DoesNotExist:
            try:
                # Если не нашли по email, ищем по username
                user = UserModel.objects.get(username=username)
            except UserModel.DoesNotExist:
                return None
        else:
            if user.check_password(password):
                return user
        return None