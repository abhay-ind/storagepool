from django.contrib import admin
from django.urls import path


from .views import login_view, register_view, logout_view

urlpatterns = [
    path('accounts/login/', login_view),
    path('accounts/register/', register_view),
    path('accounts/logout/', logout_view)
]
