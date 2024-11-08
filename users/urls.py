from django.contrib import admin
from django.urls import include, path
from . import views
from users import views as user_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("register/", user_views.register, name="register"),
    path("login/", auth_views.LoginView.as_view(template_name="users/login.html"), name="login"),
    path("logout/", user_views.CustomLogoutView.as_view(template_name="users/logout.html"), name="logout"),
    path("profile/", user_views.profile, name="profile"),
]