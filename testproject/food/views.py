"""
Docstrings R us!!
"""

from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    """
    Docstrings R us!!
    """
    return HttpResponse('hello bitches')


def item(request):
    """
    Docstrings R us!!
    """
    return HttpResponse('item view baby!!')
