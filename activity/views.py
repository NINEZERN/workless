# from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.views.decorators.http import require_POST


# Create your views here.
def hello(request):
    return HttpResponse(b"Hello world")

@login_required
@require_POST
def start_session(request):
    return HttpResponse(b"STARTING SESSION")

