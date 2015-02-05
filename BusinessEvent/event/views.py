from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from models import *
from mimetypes import guess_type
from django.contrib.auth.decorators import login_required
from django.db import transaction
from datetime import datetime

def home(request):
    newss = News.objects.all().order_by("-datetime")
    context = {'newss':newss}
    if not request.user.is_anonymous():
        user_more = User_More.objects.get(user=request.user)
        context['login_user'] = user_more
    return render(request, 'event/index.html', context)

def contact(request):
    context = {}
    if not request.user.is_anonymous():
        user_more = User_More.objects.get(user=request.user)
        context['login_user'] = user_more
    return render(request, 'event/contact.html', context)

@login_required
def my_events(request):
    usermore = User_More.objects.get(user=request.user)
    context = {'login_user': usermore}
    user_events = UserMore_Event.objects.filter(user_more=usermore)
    events = [user_event.event for user_event in user_events]
    context['events'] = events
    return render(request, 'event/my_events.html', context)

@login_required()
def my_friends(request):
    usermore = User_More.objects.get(user=request.user)
    context = {'login_user': usermore}
    user_events = UserMore_Event.objects.filter(user_more=usermore)
    events = [user_event.event for user_event in user_events]
    friends = {}
    for event in events:
        pairs = UserMore_Event.objects.filter(event=event)
        for pair in pairs:
            if not pair.user_more in friends:
                friends[pair.user_more] = 0
    if usermore in friends:
        friends.pop(usermore)
    context['friends'] = friends
    return render(request, 'event/my_friends.html', context)

@transaction.atomic
@login_required()
def publish(request):
    user_more = User_More.objects.get(user=request.user)
    context = {'login_user': user_more}
    if request.method == 'GET':
        return render(request, 'event/register.html', context)
    news = News(title=request.POST['title'], tag=request.POST['tag'], abstract=request.POST['abstract'], content=request.POST['content'], pic=request.FILES['picture'], media=request.user, check=True, datetime=datetime.now())
    news.save()
    return redirect('/news')

@transaction.atomic
@login_required()
def new_event(request):
    user_more = User_More.objects.get(user=request.user)
    context = {'login_user': user_more}
    if user_more.role != 4:
        return redirect('/news')
    if request.method == 'GET':
        return redirect('new_event/')
    e_name = request.POST['name']
    e_tag = request.POST['tag']
    e_place = request.POST['place']
    e_description = request.POST['description']
    guest_list = request.REQUEST.getlist('guests')
    e_pic = request.FILES['picture']
    event = Event(name=e_name, tag=e_tag, description=e_description, pic=e_pic, datetime=datetime.now(), place = e_place)
    event.save()
    print 'guest_list',guest_list
    print 'here'
    for i in guest_list:
        e_user_more = User_More.objects.get(id=i)
        pair = UserMore_Event(user_more=e_user_more, event=event)
        pair.save()
    return redirect('/all_events')


@login_required()
def all_user(request):
    user_more = User_More.objects.get(user=request.user)
    if user_more.role != 3 and user_more.role != 4:
        return redirect('/news')
    context = {'login_user': user_more}
    all_users = User_More.objects.all()
    context['friends'] = all_users
    return render(request, 'event/my_friends.html', context)

@login_required()
def all_event(request):
    user_more = User_More.objects.get(user=request.user)
    if user_more.role != 3 and user_more.role != 4:
        return redirect('/news')
    context = {'login_user': user_more}
    all_event = Event.objects.all().order_by('-datetime')
    context['events'] = all_event
    return render(request, 'event/my_events.html', context)