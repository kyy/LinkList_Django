from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import URL_listForm


@login_required
def main_page(request):
    form = URL_listForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.user = request.user
            new_post.save()
            return redirect(to="main")
    return render(request, 'link/main.html', {'form':form})






