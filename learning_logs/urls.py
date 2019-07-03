from django.conf.urls import url
from django.urls import path
from django.urls import re_path
from . import views

app_name = 'leaning_logs'
urlpatterns = [
    # 主页 r'^$' 这个正则表达式让Python查找开头和末尾之间没有任何东西的URL,r让Python将接下来的字符串视为原始字符串
    # url(r'^$', views.index, name='index'),

    path('', views.index, name='index'),
    path('topics/', views.topics, name='topics'),
    re_path('topics/(?P<topic_id>\d+)/', views.topic, name='topic'),

    # 新建topic
    path('new_topic/', views.new_topic, name='new_topic'),
    # 新建entry
    re_path('new_entry/(?P<topic_id>\d+)/', views.new_entry, name='new_entry'),
    # 编辑entry
    re_path('edit_entry/(?P<entry_id>\d+)/', views.edit_entry, name='edit_entry'),
]
