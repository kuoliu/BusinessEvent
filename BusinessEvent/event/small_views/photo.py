__author__ = 'lk'

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from event.models import *
from mimetypes import guess_type

def user_photo(request, user_id):
    u = get_object_or_404(User, id=user_id)
    user_more = get_object_or_404(User_More, user=u)
    if not user_more:
        raise Http404

    content_type = guess_type(user_more.pic.name)
    return HttpResponse(user_more.pic.read(), content_type=content_type)