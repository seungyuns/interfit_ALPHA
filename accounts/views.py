from django.shortcuts import render, redirect
from django.contrib.auth.models import User # 계정 클래스
from django.contrib import auth # 계정 권한 클래스

#회원관리기능

def signup(request):

    if request.method == 'POST':  # 포스트 방식의 요청이 들어오면.
        if request.POST['password1'] == request.POST['password2']: #password1 과2 가 같으면
            user = User.objects.create_user(username=request.POST['username'], password = request.POST['password1']) 
            auth.login(request, user) #계정을 생성해주고, 회원가입이되면 바로 로그인이 되도록 한다.
            return redirect('home')
    return render(request, 'signup.html')

    return render(request, 'signup.html')
def login(request):

    if request.method == 'POST': #포스트 방식 요청이 들어오면
        username = request.POST['username'] 
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password) # 우리 회원이 맞는지 확인하고 맞다면 user변수에 회원 담기.

        if user is not None: 
            auth.login(request, user) #존재하는 회원이면 로그인하고 권한을 준다.
            return redirect('resume_index')
        else:
            return render(request, 'login.html', {'error': 'username or password is incorrect.'}) #아니면 에러 출력 
    else:
        return render(request, 'login.html') #다른 에러가나면 로그인창에 계속 머물게하기.

    return render(request, 'login.html')

def logout(request):
    auth.logout(request) #User 클래스 로그아웃 함수 실행.
    return render(request, 'resume_index.html')
