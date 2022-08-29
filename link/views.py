from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect

from . import forms
from .forms import URL_listForm
from .models import URL_list

@login_required
def main_page(request):
    form = URL_listForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            name = form.cleaned_data['name']
            if URL_list.objects.filter(user=request.user, name=name).exists():
                raise ValidationError(' o lo l o l o ')
            new_post = form.save(commit=False)
            new_post.user = request.user
            new_post.save()
            return redirect(to="main")
    return render(request, 'link/main.html', {'form': form})








