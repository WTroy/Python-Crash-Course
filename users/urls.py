from django.conf.urls import url
from django.urls import path
from django.contrib.auth.views import LoginView
from django.urls import re_path
from . import views

app_name = 'users'
urlpatterns = [
    # 而单词 login让它将请求发送给Django默认视图login (请注意，视图实参为login ，而不是views.login )。django2.x 默认视图变为 LoginView
    # 鉴于我们没有编写自己的视图函数，我们传递了一个字典，告诉Django 去哪里查找我们将编写的模板
    # path('login/', LoginView, {'template_name': 'users/login.html'}, name='login'),
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
]
