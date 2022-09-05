from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

from .forms import MyUserCreationForm, MyAuthenticationForm
from django.views.generic import CreateView
from django.shortcuts import render, redirect
from django.contrib import messages


def home(request):
    return render(request, "registration/home.html")


class SignUp(CreateView):
    form_class = MyUserCreationForm
    initial = {'key': 'value'}
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to="login")
        return render(request, self.template_name, {'form': form})

# def SignUp(request):
#     if request.method == 'POST':
#         form = MyUserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             messages.success(request, f'Создан аккаунт {username}!')
#             return redirect('login')
#     else:
#         form = MyUserCreationForm()
#
#     return render(request, 'registration/signup.html', {'form': form})


class LogIn(LoginView):
    form_class = MyAuthenticationForm
    initial = {'key': 'value'}
    success_url = reverse_lazy("home")
    template_name = "registration/login.html"

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

# def LogIn(request):
#     form = MyAuthenticationForm(request.POST)
#     context = {}
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect("dashboard")
#         else:
#             context['error'] = "Логин или пароль неправильные"
#
#     return render(request, 'registration/login.html', context, {
#         'form': form,
#     })
