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
from event.small_views.utils import public_ip

@transaction.atomic
def login(request):
    context = {}
    if request.method == 'GET':
        return render(request, 'event/login.html', context)
    errors = []
    context['errors'] = errors

    new_user = authenticate(username=request.POST['username'], \
                            password=request.POST['password'])
    if not new_user:
        errors.append("User or password is false")
        return render(request, 'event/login.html', context)
    elif not new_user.is_active:
        errors.append('User is not activated')
        return render(request, 'event/login.html', context)
    else:
        django.contrib.auth.login(request, new_user)
    user_more = User_More.objects.get(user=new_user)
    return redirect('/event')

@transaction.atomic
def register(request):
    context = {}
    if request.method == 'GET':
        return render(request, 'event/register.html', context)
    if len(User.objects.filter(username=request.POST['email'])) > 0:
        context['error'] = 'User Already Exist'
        return render(request, 'event/small_pages/error.html', context)
    if request.POST['password1'] != request.POST['password2']:
        context['error'] = "Passwords don't match"
        return render(request, 'event/small_pages/error.html', context)
    #csock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    #csock.connect(('8.8.8.8', 80))
    #(myaddr, myport) = csock.getsockname()
    myaddr = public_ip()
    try:
        random_str = gen_activate_key(20)
        subject = 'Blog registration confirmation'
        message = 'please follow this link to complete registration %(url)s/%(username)s/%(random_str)s' \
                  % {'url': 'http://' + myaddr + ':8000/event/activate',
                     'username': request.POST['email'],
                     'random_str': random_str}
        sender = '4129802587lk@gmail.com'
        receiver = [request.POST['email']]
        send_mail(subject, message, sender, receiver, )
    except:
        context['error'] = 'Invalid Email Address'
        return render(request, 'event/small_pages/error.html', context)
        # Creates the new user from the valid form data
    try:
        new_user = User.objects.create_user(username=request.POST['email'], \
                                        first_name=request.POST['firstname'], \
                                        last_name=request.POST['lastname'], \
                                        email=request.POST['email'], \
                                        password=request.POST['password1'], )
    except:
        context['error'] = 'Information not enough, please complete the form'
        return render(request, 'event/small_pages/error.html', context)
    new_user.is_active = False
    new_user.save()
    new_user_random = User_Random(user=new_user, random=random_str)
    new_user_random.save()
    try:
        new_user_more = User_More(user=new_user, description=request.POST['description'], pic=request.FILES['picture'], role=1)
    except:
        context['error'] = 'Information not enough, please complete the form'
        return render(request, 'event/small_pages/error.html', context)
    new_user_more.save()
    return redirect('/event/confirmation')

@login_required
@transaction.atomic
def modify_info(request):
    user_more = User_More.objects.get(user = request.user)
    context = {'login_user': user_more}
    if request.method == 'GET':
        return render(request, 'event/personal_info.html', context)
    if request.POST['password1'] != request.POST['password2']:
        context['error'] = "Passwords don't match"
        return render(request, 'event/register.html', context)
    user_more.user.first_name = request.POST['firstname']
    user_more.user.last_name = request.POST['lastname']
    user_more.user.password = request.POST['password1']
    user_more.user.email = request.POST['email']
    user_more.user.username = request.POST['email']
    user_more.classification = request.POST['classification']
    try:
        t = request.FILES['picture']
    except:
        pass
    else:
        user_more.pic = request.FILES['picture']
    user_more.description = request.POST['description']
    user_more.user.save()
    user_more.save()
    return redirect('/event/modify_info/')

@transaction.atomic
def activate(request, user_email, random_id):
    u = User.objects.get(username=user_email)
    u_r = User_Random.objects.get(user_id=u.id)

    if u_r.random == random_id:
        u.is_active = True
        u.save()
        return redirect('/event/login')
    else:
        return redirect('/event/confirmation')

def gen_activate_key(length):
    chars = string.ascii_letters + string.digits
    return ''.join([random.choice(chars) for i in range(length)])

def confirmation(request):
    return render(request, 'event/small_pages/confirmation.html')

def search(request):
    all_event = Event.objects.all()
    try:
        search_txt = request.POST['searchtxt'].lower()
    except:
        search_txt = ""
    events = []
    for e in all_event:
        if e.description.lower().find(search_txt) >= 0:
            events.append(e)
    context = {}
    if not request.user.is_anonymous():
        user_more = User_More.objects.get(user=request.user)
        context['login_user'] = user_more
    context['events'] = events
    return render(request, 'event/my_events.html', context)


