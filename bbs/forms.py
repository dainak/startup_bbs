from django import forms
from .models import Reply, Topic

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ["category", "comment"]

class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ["target", "comment"]