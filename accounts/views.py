# accounts/views.py
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect(settings.LOGIN_URL) # default: "/accoutns/login/"
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup_form.html',{
        'form': form,
    })

def login(request):
    pass

@login_required # 데코레이터 혹은 장식자. 함수를 감싸줌. wrapping. 
def profile(request):
    return render(request, 'accounts/profile.html')
