from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import URL_listForm
from .models import URL_list

@login_required
def main_page(request):
    form = URL_listForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            name = form.cleaned_data['name']
            if URL_list.objects.filter(user=request.user, name=name).exists():
                return HttpResponse('Same data already added, change name')
            new_post = form.save(commit=False)
            new_post.user = request.user
            new_post.save()
            return HttpResponse("Data added")
    return render(request, 'link/main.html', {'form': form})








