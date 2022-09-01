from django import forms
from .models import URL_list


class URL_listForm(forms.ModelForm):
    required_css_class = "field"
    error_css_class = "error"

    class Meta:
        model = URL_list
        fields = ("name", "URL_long")
