# accounts/views.py
from django.conf import settings
from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm # 사용자 인증 커스텀시 제거
from django.contrib.auth.decorators import login_required
from .forms import SignupForm

def signup(request):
    if request.method == 'POST':
        # form = UserCreationForm(request.POST)
        form = SignupForm(request.POST) # 사용자 인증 커스텀시 UserCreationForm을 상속받은 커스텀form으로 진행
        if form.is_valid():
            user = form.save()
            return redirect(settings.LOGIN_URL) # default: "/accoutns/login/"
    else:
        form = SignupForm()
    return render(request, 'accounts/signup_form.html',{
        'form': form,
    })

def login(request):
    pass

@login_required # 데코레이터 혹은 장식자. 함수를 감싸줌. wrapping. 
def profile(request):
    return render(request, 'accounts/profile.html')
