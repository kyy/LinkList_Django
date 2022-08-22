from .forms import MyUserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.shortcuts import render, redirect


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



