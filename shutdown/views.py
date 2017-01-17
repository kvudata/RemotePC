from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.

def show_controls(req):
    return render(req, 'shutdown/controls.html')

def suspend(req):
    return HttpResponse('suspending!')
