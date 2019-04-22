from django.shortcuts import render
from django.contrib.auth.models import User
from .forms import RegisterForm, LoginForm, UserProfileUpdateForm, UserPasswordChangeForm2
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.shortcuts import render, reverse, HttpResponseRedirect, get_object_or_404

from django.contrib import messages


# Create your views here.


def user_login(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                msg = "Merhabalar {} sisteme Hoş geldiniz".format(username)
                messages.success(request, msg, extra_tags='success')
                return HttpResponseRedirect(reverse('post-list'))

    return render(request, 'auths/login.html', context={'form': form})


def user_logout(request):
    username = request.user.username
    logout(request)
    msg = " <b>Sistemden çıkış yaptınız. Güle güle {}</>".format(username)
    messages.success(request, msg, extra_tags='success')
    return HttpResponseRedirect(reverse('user-login'))


# def register(request):
#     form = RegisterForm(data=request.POST or None)
#     if form.is_valid():
#         user = form.save(commit=False)
#         username = form.cleaned_data.get('username')
#         password = form.cleaned_data.get('password')
#         user.set_password(password)
#         user.save()
#         user = authenticate(username=username, password=password)
#         if user is not None:
#             if user.is_active:
#                 login(request, user)
#                 messages.success(request, '<b> Tebrikler Kayıt İlemi Başarılı</>', extra_tags='success')
#                 return HttpResponseRedirect(user.userprofile.get_user_profile_url())
#
#     return render(request, 'auths/register.html', context={'form': form})
