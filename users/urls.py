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
    path('edit-profile/', views.edit_profile_view, name='edit_profile'),
    path('delete-account/', views.delete_account_view, name='delete_account'),
    path('terms_conditions/', views.terms_conditions, name='terms_conditions'),
]