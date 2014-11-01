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
    return redirect('/event')

@transaction.atomic
def register(request):
    context = {'login_user': request.user}
    if request.method == 'GET':
        return render(request, 'event/register.html', context)
    if len(User.objects.filter(username=request.POST['email'])) > 0:
        context['error'] = 'User Already Exist'
        return render(request, 'event/register.html', context)
    if request.POST['password1'] != request.POST['password2']:
        context['error'] = "Passwords don't match"
        return render(request, 'event/register.html', context)
    csock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    csock.connect(('8.8.8.8', 80))
    (myaddr, myport) = csock.getsockname()
    try:
        random_str = gen_activate_key(20)
        subject = 'Blog registration confirmation'
        message = 'please follow this link to complete registration %(url)s/%(username)s/%(random_str)s' \
                  % {'url': 'http://' + myaddr + ':8000/event/activate',
                     'username': request.POST['email'],
                     'random_str': random_str}
        sender = 'kuokuo001@gmail.com'
        receiver = [request.POST['email']]
        send_mail(subject, message, sender, receiver, )
    except:
        context['error'] = 'Invalid Email Address'
        return render(request, 'event/register.html', context)
        # Creates the new user from the valid form data
    new_user = User.objects.create_user(username=request.POST['email'], \
                                        first_name=request.POST['firstname'], \
                                        last_name=request.POST['lastname'], \
                                        email=request.POST['email'], \
                                        password=request.POST['password1'], )
    new_user.is_active = False
    new_user.save()
    new_user_random = User_Random(user=new_user, random=random_str)
    new_user_random.save()
    new_user_more = User_More(user=new_user, description=request.POST['description'], pic=request.FILES['picture'])
    new_user_more.save()
    return redirect('/event/confirmation')

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
    return render(request, 'event/confirmation.html')


