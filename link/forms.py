from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import URL_list


# class MultilinkField(forms.Field):
#     def to_python(self, value):
#         """Normalize data to a list of strings."""
#         # Return an empty list if no input was given.
#         if not value:
#             return []
#         return value.split('\n')
#
#     def validate(self, value):
#         """Check if value consists only of valid emails."""
#         # Use the parent's handling of required fields, etc.
#         super().validate(value)
#         for url in value:
#             URLValidator(url)

class URL_listForm(forms.ModelForm):
    # def clean(self):
    #     cleaned_data = super().clean()
    #     name = cleaned_data.get("name")
    #     if URL_list.objects.filter(user=self.user, name=name).exists():
    #         raise ValidationError(' o lo l o l o ')

    class Meta:
        model = URL_list
        fields = ("name", "URL_long")

