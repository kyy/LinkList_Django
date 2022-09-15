from django import forms
from .models import URL_list
from django.utils.translation import gettext_lazy as _


class URL_listForm(forms.ModelForm):
    name = forms.CharField(label=_('Имя страницы'), max_length=100)
    URL_long = forms.CharField(widget=forms.Textarea, label=_('Вставьте ссылки через пробел или с новой строки'), max_length=10000)
    required_css_class = "field"
    error_css_class = "error"

    class Meta:
        model = URL_list
        fields = ("name", "URL_long")
