from django import forms
from django.forms import ModelForm
from .models import Entry, Topic

class TopicForm(ModelForm):
    class Meta :
        model = Topic
        fields = ['text'] 
        labels = {'text':''}

class EntryForm(ModelForm):
    class Meta :
        model = Entry
        fields = ['text']
        label = {'text':''}
        widgets = {'text': forms.Textarea(attrs={'col':80})}