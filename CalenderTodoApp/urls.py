from django.urls import path
from .views import loginfunc, admin_loginfunc, logoutfunc, activ_listfunc, signupfunc, TodoCreate, calenderfunc

urlpatterns = [
    path('', loginfunc, name='login'),
    path('login/', loginfunc, name='login'),
    path('admin_login/', admin_loginfunc, name='admin_login'),
    path('logout/', logoutfunc, name='logout'),
    path('signup/', signupfunc, name='signup'),
    path('activ_list/', activ_listfunc, name='activ_list'),
    path('calender/', calenderfunc, name='calender'),
    path('todo/', TodoCreate.as_view(), name='todo'),
]
