from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import login

from users.forms import ProfileForm

@login_required
def profile(request):
    form = ProfileForm(request.POST or None, instance=request.user)
    if form.is_valid():
        form.save()
        messages.success(request, '編輯個人檔案成功!')

    return render(request, 'users/profile.html', {'form': form})

def password_change_done(request):
    messages.success(request, '密碼編輯成功!')
    return redirect('users:profile')

def register(request):
    if request.user.is_authenticated:
        messages.warning(request, f'已經以 {request.user.username} 登入了')
        return redirect('users:profile')

    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        user = form.save()
        login(request, user)
        messages.success(request, '註冊成功')
        return redirect('users:profile')

    return render(request, 'users/register.html', {'form': form})

def password_reset_done(request):
    messages.success(request, '已寄出密碼重設信件!')
    return redirect('users:login')

def passeord_reset_complete(request):
    messages.success(request, '密碼重設成功!')
    return redirect('users:login')