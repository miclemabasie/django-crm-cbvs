from django.shortcuts import render
from django.urls import reverse
from django.views.generic import CreateView
from .models import User
from .forms import UserCreateForm


class UserCreateView(CreateView):
    template_name = 'registration/signup.html'
    form_class = UserCreateForm

    def get_success_url(self) -> str:
        return reverse('accounts:login')


    def form_valid(self, form):
        return super(UserCreateView, self).form_valid(form)