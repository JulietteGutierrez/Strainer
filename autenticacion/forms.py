from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import Usuario

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = Usuario
        fields = ("username", "email","first_name","last_name")

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = Usuario
        fields = ("username", "email","first_name","last_name")        




# class Registroform(UserCreationForm):
#     class Meta:
#         model = User
#         field = [
#             'username',
#             'first_name',
#             'last_name',
#             'email',
#         ]
#         label = {
#             'username' : 'Nombre de usuario',
#             'first_name': 'Nombre',
#             'last_name' :'Apellido',
#             'email': 'Correo electronico',
#         }