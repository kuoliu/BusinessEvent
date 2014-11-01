from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from models import *
from mimetypes import guess_type
from django.contrib.auth.decorators import login_required
from django.db import transaction

def home(request):
    return render(request, 'event/index.html')

def contact(request):
    return render(request, 'event/contact.html')
