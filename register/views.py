# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm

# Create your views here.

# Create your views here.
def register(request):
    if request.method == "POST":
         form = UserRegisterForm(request.POST)
         if form.is_valid():
             form.save()
             username = form.cleaned_data.get('username')
             messages.success(request, 'Your account is created! You can now login. ')
             return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request,'register/register.html',{'form': form})

@login_required
def profile(request):
    return render(request, 'register/profile.html')
