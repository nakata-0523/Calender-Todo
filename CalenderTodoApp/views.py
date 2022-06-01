from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.db import IntegrityError  #登録ユーザー重複
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .models import TodoModel

# Create your views here.
def signupfunc(request):#ユーザーの新規作成
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.create_user(username, '', password)#新規ユーザーの登録
            return redirect('activ_list')

        except IntegrityError: #登録ユーザーの重複
            return render(request, 'signup.html', {'error':'このユーザーはすでに登録されています。'})

    return render(request, 'signup.html', {})

def loginfunc(request):
    if request.method == "POST":#リクエストの判定
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:#ログイン成功
            login(request, user)
            return redirect('calender')
        else:#ログイン失敗
            return render(request, 'login.html', {})
    return render(request, 'login.html', {})#リクエストがGETの時

def admin_loginfunc(request):
    if request.method == "POST":#リクエストの判定
        username = request.POST['username']
        password = request.POST['password']
        object_list = User.objects.all()

        user = authenticate(request, username=username, password=password)

        for item in object_list: #管理者判定
            if item.is_superuser == True:
                admin_user = item

        if user == admin_user:#ログイン成功
            login(request, user)
            return redirect('activ_list')
        else:#ログイン失敗
            return render(request, 'admin_login.html', {})
    return render(request, 'admin_login.html', {})#リクエストがGETの時

def logoutfunc(request): #ログアウト機能
    logout(request)
    return redirect('login')

def activ_listfunc(request): #管理者画面　ユーザー一覧
    object_list = User.objects.all()
    login_user = request.user
    activ_list = []
    
    for item in object_list:
        if item.is_superuser == False: #管理者の判定
            activ_list.append(item)
    
    return render(request, 'activ_list.html', {'activ_list':activ_list, 'login_user':login_user})

def calenderfunc(request): #カレンダー画面
    object_list = User.objects.all()
    login_user = request.user
    
    return render(request, 'calender.html', {})

class TodoCreate(CreateView): #Todo機能
    template_name = 'todo.html'
    model = TodoModel
    fields = ('user_id', 'suthor_id', 'todo', '')
    success_url = reverse_lazy('list')
