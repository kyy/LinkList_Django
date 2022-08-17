from django import forms
from django.contrib.auth.forms import UserCreationForm
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

