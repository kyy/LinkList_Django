from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError




class MyUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
# checking for unique email:
    def clean_email(self):
        email = self.cleaned_data['email'].strip()
        if User.objects.filter(email__iexact=email).exists():
            raise ValidationError('A user with that e-mail already exists.')
        return email

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

class MyAuthenticationForm(AuthenticationForm):
# checking for username  in DB:
    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            raise forms.ValidationError(f"The {username} is incorrect username.")
        return username
# checking for password in DB:
    def clean_password(self):
        password= self.cleaned_data['password']
        try:
            User.objects.get(password=password)
        except User.DoesNotExist:
            raise forms.ValidationError("Password is incorrect.")
        return password


