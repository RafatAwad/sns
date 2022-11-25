from .models import UserProfile,User
from .forms import ProfileForm, AdminLoginForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.utils.translation import gettext as _

@login_required
def profile(request, user_id):
    profile = UserProfile.objects.get(user_id=user_id)
    context = {
        'profile': profile
    }
    return render(request, 'account/profile.html', context)

@login_required
def update_profile(request, user_id):
    profile = UserProfile.objects.get(id=user_id)
    forms = ProfileForm(instance=profile)
    if request.method == 'POST':
        forms = ProfileForm(request.POST, request.FILES, instance=profile)
        if forms.is_valid():
            forms.save()
    context = {
        'forms': forms
    }
    return render(request, 'account/update-profile.html', context)

def admin_login(request):
    form = AdminLoginForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            human = True
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                messages.success(request,_("Login successfull"))
                return redirect('home')
        messages.error(request,_('Invalid credentials, Please check username/email or password. '))
    context = {'form': form}
    return render(request, 'account/login.html', context)

@login_required
def admin_logout(request):
    logout(request)
    return redirect('login')
@login_required
def settings_page(request):
    context ={}
    return render(request, 'settings.html', context)
