__author__ = 'lk'

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from event.models import *
from django.db import transaction
import random, string
import socket
from django.core.mail import send_mail
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
import django

def news_page(request, news_id):
    usermore = User_More.objects.get(user=request.user)
    context = {'login_user': usermore}
    news = News.objects.get(id=news_id)
    context['news'] = news
    return render(request, 'event/news_page.html', context)

@login_required()
def user_page(request, user_id):
    usermore = User_More.objects.get(user=request.user)
    context = {'login_user': usermore}
    u = User.objects.get(id=user_id)
    user_more = User_More.objects.get(user=u)
    context['cur_user'] = user_more
    return render(request, 'event/user_page.html', context)

@login_required()
def event_page(request, event_id):
    usermore = User_More.objects.get(user=request.user)
    context = {'login_user': usermore}
    event = Event.objects.get(id=event_id)
    userevents = UserMore_Event.objects.filter(event=event)
    guests = [ue.user_more for ue in userevents]
    print guests
    context['event'] = event
    context['guests'] = guests
    return render(request, 'event/event_page.html', context)

@login_required()
def publish_news(request):
    usermore = User_More.objects.get(user=request.user)
    context = {'login_user': usermore}
    if usermore.role != 2:
        return redirect('/news')
    return render(request, 'event/small_pages/publish_news.html', context)

@login_required()
def publish_event(request):
    usermore = User_More.objects.get(user=request.user)
    context = {'login_user': usermore}
    if usermore.role != 4:
        return redirect('/news')
    all_users = User_More.objects.all()
    context['all_users'] = all_users
    return render(request, 'event/small_pages/publish_event.html', context)