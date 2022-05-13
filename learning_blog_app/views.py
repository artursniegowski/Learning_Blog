from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse 
from django.contrib.auth.decorators import login_required

from .models import Topic, Entry
from .forms import EntryForm, TopicForm
# Create your views here.

def index(request):
    """The homepage for Learning blog app"""
    return render(request,'learning_blog_app/index.html')

@login_required
def topics(request):
    """Show all topics"""
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {'topics': topics}
    return render(request,'learning_blog_app/topics.html',context)

@login_required
def topic(request, topic_id : int):
    """Show a single topic and all its entries"""
    topic = get_object_or_404(Topic,id=topic_id)
    # Making sure the topic belongs to the current user
    check_topic_owner(topic,request)

    entries = topic.entry_set.order_by('-date_added')
    context = {'topic':topic, 'entries':entries}
    return render(request,'learning_blog_app/topic.html',context)

@login_required
def new_topic(request):
    """Add new topic"""
    if request.method != 'POST':
        # No data submitted, create a blank form.
        form = TopicForm()
    else:
        # POST data submited, process data.
        form = TopicForm(request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return HttpResponseRedirect(reverse('learning_blog_app:topics'))

    context = {'form': form}
    return render(request,'learning_blog_app/new_topic.html',context)

@login_required    
def new_entry(request, topic_id : int):
    """Add a new entry for a particular topic"""
    topic = get_object_or_404(Topic,id=topic_id)
    
    # Making sure the topic belongs to the current user
    check_topic_owner(topic,request)

    if request.method != 'POST':
        # No data submitted, create a blank form.
        form = EntryForm()
    else:
        # POST data submited, process data.
        form = EntryForm(request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse('learning_blog_app:topic',args=[topic_id]))

    context = {'topic':topic, 'form':form }
    return render(request,'learning_blog_app/new_entry.html',context)

@login_required
def edit_entry(request, entry_id : int):
    """Edit an existing entry"""
    entry = get_object_or_404(Entry,id=entry_id)
    topic = entry.topic

    # Making sure the entry belongs to the current user
    check_topic_owner(topic,request)

    if request.method != 'POST':
        # Intial request , pre fill the current entry
        form = EntryForm(instance=entry)
    else :
        # POST data submitted, process data
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learning_blog_app:topic',args=[topic.id]))

    context = {'entry':entry, 'topic':topic, 'form':form}
    return render(request,'learning_blog_app/edit_entry.html',context)

def check_topic_owner(topic : Topic.objects,request) -> None:
    """checking if the topic owner is the current usser"""
    """raise an exception if it dosent match"""
    if topic.owner != request.user:
        raise Http404