from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from accounts.forms import UserSignUpForm 

# The forms.py will call these views
class SignUpView(CreateView):
    form_class = UserSignUpForm
    success_url = reverse_lazy("login")
    template_name = "accounts/signup.html"
 
