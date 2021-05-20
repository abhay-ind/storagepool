from django.shortcuts import render, redirect

from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout
)

from .forms import UserLoginForm, UserRegisterForm
from rest_framework.response import Response
from rest_framework import serializers, viewsets, status



def login_view(request):
    next = request.GET.get('next')
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        if next:
            return redirect(next)
        return redirect('/')

    context = {
        'form': form,
    }
    # return  Response(form, status=status.HTTP_202_ACCEPTED)
    return render(request, "login.html", context)


def register_view(request):
    next = request.GET.get('next')
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)
        if next:
            return redirect(next)
        return redirect('/')

    context = {
        'form': form,
    }
    # return Response(form, status=status.HTTP_201_CREATED)
    return render(request, "signup.html", context)


def logout_view(request):
    logout(request)
    # return Response(status=status.HTTP_200_OK)
    return redirect('/')