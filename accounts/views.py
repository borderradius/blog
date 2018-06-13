# accounts/views.py
from django.conf import settings
from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm # 사용자 인증 커스텀시 제거
from django.contrib.auth.decorators import login_required
from .forms import SignupForm, LoginForm

from django.contrib.auth.views import login as auth_login
from allauth.socialaccount.models import SocialApp
from allauth.socialaccount.templatetags.socialaccount import get_providers



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


@login_required # 데코레이터 혹은 장식자. 함수를 감싸줌. wrapping. 
def profile(request):
    return render(request, 'accounts/profile.html')

def login(request):
    providers = []
    
    # return에 들어갈 providers list 값을 만들어 주는 과정
    for provider in get_providers(): # settings.py/INSTALLED_APPS 내에서 활성화된 providers 목록을 가지고옴. providers.facebook , providers.kakao, providers.naver
        try:
            # 실제 Provider별 Client id/secret 이 등록이 되어 있는가?
            provider.social_app = SocialApp.objects.get(provider=provider.id, sites=settings.SITE_ID)
        except SocialApp.DoesNotExist:
            provider.social_app = None
        providers.append(provider)

    # django lovin view 에 넘길 값들 정의
    return auth_login(request,
        authentication_form = LoginForm,
        template_name = 'accounts/login_form.html',
        extra_context = {'providers': providers})