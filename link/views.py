import re
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from ratelimit.decorators import ratelimit
from django.contrib import messages
from .forms import URL_listForm
from .models import URL_list
from datetime import datetime
from django.utils.translation import gettext as _

now = datetime.now()
now = now.strftime("%Y-%m-%d")

@ratelimit(method='POST', block=True, rate='10/m', key='user')
@login_required
def new_url(request):
    form = URL_listForm(request.POST)
    if request.method == "POST":
        if form.is_valid() and URL_list.objects.filter(user=request.user,
                                                       data__year=now[0:4],
                                                       data__month=now[5:7],
                                                       data__day=now[8:10]
                                                       ).count()<3: # 3 link a day for free users
            name = form.cleaned_data['name']
            if URL_list.objects.filter(user=request.user, name=name).exists():
                messages.warning(request, _(f'Запись с "{name}" именем уже добавлена, измениите имя'))
                return redirect('main')
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('dashboard')
        else:
            messages.warning(request, 'Вы можете создавать только 3 странички в день, обновите аккуант, если хотите больше возможностей')
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
    # page = paginator.page(int(request.GET.get('page', 1)))
    return render(request, 'link/dashboard.html', {
        'urls': urls,
        'page_obj': page_obj,
        # 'page': page,
    })


def show_urls(request, url_short):
    urls = None
    url_dict = None
    try:
        urls = URL_list.objects.get(URL_short=url_short)
        url_dict = urls.URL_long
        regex = r'(https?://[^\"\s>]+)'
        matches = re.finditer(regex, url_dict, re.MULTILINE)
        url_dict = []
        i=0
        for match in matches:
            i+=1
            url_dict.append(match.group())
        if i>5 and request.user.is_authenticated:
            messages.warning(request, _(f'На вашей страничке "{urls.name}" отображается не более 5 ссылок, обновите аккуант, если хотите больше возможностей'))
        url_dict = url_dict[0:5] # 5 link for regular users
    except ObjectDoesNotExist:
        redirect('dashboard')
    return render(request, 'link/showurls.html', {
        'urls': urls,
        'url_dict': url_dict,
    })


@ratelimit(method='POST', block=True, rate='10/m', key='user')
@login_required
def edit_url(request, url_short):
    post = get_object_or_404(URL_list.objects.filter(URL_short=url_short, user=request.user))
    if request.method == "POST":
        form = URL_listForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            messages.success(request, _(f'Ваши данные в "{post.name}" обновлены'))
            return redirect('dashboard')
    else:
        form = URL_listForm(instance=post)
    return render(request, 'link/link.html', {
        'form': form,
    })


@ratelimit(method='POST', block=True, rate='10/m', key='user')
@login_required
def delete_url(request, url_short):
    post = get_object_or_404(URL_list.objects.filter(URL_short=url_short, user=request.user))
    if request.method == "POST":
        post.delete()
        messages.success(request, _(f'Ваша страничка "{post.name}" удалена'))
        return redirect('dashboard')
    return render(request, 'link/delete_confirm.html')
