from django.shortcuts import render
from .models import Topic, Entry
from .forms import TopicForm, EntryForm
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    """学习笔记主页"""
    return render(request, 'learning_logs/index.html')


@login_required
def topics(request):
    """主题详情"""
    # topic_list = Topic.objects.order_by('date_added')
    topic_list = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {'topics': topic_list}
    return render(request, 'learning_logs/topics.html', context)


@login_required
def topic(request, topic_id):
    """显示单个主题及列表内容"""
    topic_ = Topic.objects.get(id=topic_id)
    # 确认请求的主题属于当前用户
    if topic_.owner != request.user:
        raise Http404
    entries = topic_.entry_set.order_by('-date_added')
    context = {'topic': topic_, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)


@login_required
def new_topic(request):
    """新增主题"""
    if request.method != 'POST':
        # 未提交数据，创建一个新表单
        form = TopicForm()
    else:
        # 我们使用用户输入的数据(它们存储在request.POST 中)创建一个TopicForm 实例
        form = TopicForm(request.POST)
        # 函数is_valid() 核实用户填写了所有必不可少的字段(表单字段默认都是必不可少的)，且输入 的数据与要求的字段类型一致
        if form.is_valid():
            # form.save()
            topic_ = form.save(commit=False)
            topic_.owner = request.user
            topic_.save()
            # 使用reverse() 获取页面topics 的URL，并将其传递 给HttpResponseRedirect()
            return HttpResponseRedirect(reverse('learning_logs:topics'))
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)


@login_required
def new_entry(request, topic_id):
    """在特定的主题中添加新条目"""
    topic_ = Topic.objects.get(id=topic_id)
    if request.method != 'POST':
        # 未提交数据,创建一个空表单
        form = EntryForm()
    else:
        # POST提交的数据,对数据进行处理
        form = EntryForm(data=request.POST)
        if form.is_valid():
            entry_new = form.save(commit=False)
            entry_new.topic = topic_
            entry_new.save()
            return HttpResponseRedirect(reverse('learning_logs:topic', args=[topic_id]))
    context = {'topic': topic_, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)


@login_required
def edit_entry(request, entry_id):
    """编辑既有条目"""
    entry = Entry.objects.get(id=entry_id)
    topic_ = entry.topic
    if topic_.owner != request.user:
        raise Http404
    if request.method != 'POST':
        # 初次请求，使用当前条目填充表单
        form = EntryForm(instance=entry)
    else:
        # POST提交的数据，对数据进行处理
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learning_logs:topic', args=[topic_.id]))
    context = {'entry': entry, 'topic': topic_, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)
