__author__ = 'lk'

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from event.models import *
from mimetypes import guess_type
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
default_image = os.path.join(BASE_DIR, 'static/event/images/user-pic.png')

def user_photo(request, user_id):
    u = get_object_or_404(User, id=user_id)
    user_more = get_object_or_404(User_More, user=u)
    if not user_more:
        raise Http404
    content_type = guess_type(user_more.pic.name)
    if user_more.pic == '':
        content_type = guess_type('user-pic.png')
        return HttpResponse(open(default_image).read(), content_type=content_type)
    return HttpResponse(user_more.pic.read(), content_type=content_type)