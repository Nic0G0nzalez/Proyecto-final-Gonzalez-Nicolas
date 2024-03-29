from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

#____________________________ Formulario para registrarse
class RegistroForm(UserCreationForm):
    email=forms.EmailField(required=True)
    password1=forms.CharField(label="contraseña", widget=forms.PasswordInput)
    password2=forms.CharField(label="confirmar contraseña", widget=forms.PasswordInput)

    class Meta:
        model= User
        fields=["username","password1","password2"]

#____________________________ Formulario para editar el usuario y cambiar el avatar
class UserEditForm(UserChangeForm):
    email=forms.EmailField(required=True)
    first_name=forms.CharField(label="Nombre/s", max_length=50, required=True)
    last_name=forms.CharField(label="Apellido/s", max_length=50, required=True)

    class Meta:
        model= User
        fields=["email","first_name","last_name"]

class AvatarForm(forms.Form):
    imagen= forms.ImageField(required=True)
