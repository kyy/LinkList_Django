import re
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .forms import URL_listForm
from .models import URL_list


@login_required
def new_url(request):
    form = URL_listForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            name = form.cleaned_data['name']
            if URL_list.objects.filter(user=request.user, name=name).exists():
                return HttpResponse('Same data already added, change name')
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('dashboard')
    return render(request, 'link/main.html', {
        'form': form,
    })


@login_required
def view_urls(request):
    urls = URL_list.objects.filter(user=request.user).order_by('-data')

    paginator = Paginator(urls, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    page = paginator.page(int(request.GET.get('page', 1)))

    return render(request, 'link/dashboard.html', {
        'urls': urls,
        'page_obj': page_obj,
        'page': page,
    })


def show_urls(request, url_short):
    urls = URL_list.objects.get(URL_short=url_short)
    url_dict = urls.URL_long
    regex = r'(https?://[^\"\s>]+)'
    matches = re.finditer(regex, url_dict, re.MULTILINE)
    url_dict = []
    for match in matches:
        url_dict.append(match.group())
    return render(request, 'link/showurls.html', {
        'urls': urls,
        'url_dict': url_dict,
    })


@login_required
def edit_url(request, url_short):
    post = get_object_or_404(URL_list.objects.filter(URL_short=url_short, user=request.user))
    if request.method == "POST":
        form = URL_listForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('dashboard')
    else:
        form = URL_listForm(instance=post)
    return render(request, 'link/link.html', {
        'form': form,
    })


@login_required
def delete_url(request, url_short):
    post = get_object_or_404(URL_list.objects.filter(URL_short=url_short, user=request.user))
    if request.method == "POST":
        post.delete()
        return redirect('dashboard')
    return render(request, 'link/delete_confirm.html')
