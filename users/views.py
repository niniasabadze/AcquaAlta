from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from users.models import Profile
from .forms import UserRegisterForm
from django.contrib.auth.views import LogoutView
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"Your account has been created! You can now log in!")
            return redirect("login")
    else:
        form = UserRegisterForm()
    return render(request, "users/register.html", {"form": form})

#Log Out
class CustomLogoutView(LogoutView):
    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

@login_required
def profile(request):
    return render(request, "users/profile.html")

def terms_conditions(request):
    return render(request, 'users/terms_conditions.html')

@login_required
def edit_profile_view(request):
    
    if not hasattr(request.user, 'profile'):
        Profile.objects.create(user=request.user)

    if request.method == 'POST':
        user = request.user
        user.username = request.POST.get('username', user.username)
        user.profile.user_type = ', '.join(request.POST.getlist('user_type'))
        user.save()
        user.profile.save()
        return redirect('profile')

    return render(request, 'users/edit_profile.html')

@login_required
def delete_account_view(request):
    if request.method == 'POST':
        request.user.delete()
        return redirect('home')
    return render(request, 'users/confirm_delete.html')