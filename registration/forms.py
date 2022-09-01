from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate


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
            User.objects.get(username__exact=username)
        except User.DoesNotExist:
            raise forms.ValidationError(f"The {username} is incorrect username.")
        return username

    # # checking password
    # def clean_password(self):
    #     username = self.cleaned_data.get("username")
    #     password = self.cleaned_data.get("password")
    #     if username and password:
    #         self.user_cache = authenticate(self.request, username=username, password=password)
    #         if self.user_cache is None:
    #             raise forms.ValidationError('Incorrect password')
    #         else:
    #             self.confirm_login_allowed(self.user_cache)
    #     return self.cleaned_data







