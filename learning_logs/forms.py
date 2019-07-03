from django import forms
from .models import Topic, Entry


# 我们定义了一个名为TopicForm 的类，它继承了forms.ModelForm
# 最简单的ModelForm 版本只包含一个内嵌的Meta 类，它告诉Django根据哪个模型创建表单，以及在表单中包含哪些字段
class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        # 我们根据模型Topic 创建一个表单，该表单只包含字段text
        fields = ['text']
        # 让Django不要为字段text 生成标签
        labels = {'text': ''}


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''}
        # 我们定义了属性widgets 。小部件 (widget)是一个HTML表单元素，如单行文本框、多行文本区域或下拉列表。通过设置属性widgets ，可覆盖Django选择的默认小 部件。
        # 通过让Django使用forms.Textarea ，我们定制了字段'text' 的输入小部件，将文本区域的宽度设置为80列，而不是默认的40列。这给用户提供了足够的空间，可以 编写有意义的条目
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}
