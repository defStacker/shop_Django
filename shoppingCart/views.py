# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from models import User
from django.template.response import TemplateResponse
from .models import Tool, Book, Author
# Create your views here.


def login(request):
    user_list = User.objects.order_by('andrews')[:10]
    return render(request, 'latest_books.html', {'book_list': user_list})


def logout(request):
    user_list = User.objects.order_by('andrews')[:10]
    return render(request, 'login.html', {'book_list': user_list})


def index_view(request):
    context = {}
    return TemplateResponse(request, 'index.html', context)



