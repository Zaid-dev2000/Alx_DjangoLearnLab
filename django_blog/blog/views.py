from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import login
from django.contrib import messages


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been created successfully!')
            return redirect('blog/login')
        else:
            messages.error(request, 'There was an error with your registration.')
    else:
        form = CustomUserCreationForm()
    return render(request, 'blog/register.html', {'form': form})


def base(request):
    return render(request, 'blog/base.html')

def profile(request):
    return render(request, 'blog/profile.html')