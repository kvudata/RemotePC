from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from subprocess import call

import after_response

# Create your views here.

def show_controls(req):
    return render(req, 'shutdown/controls.html')

def handle_suspend_req(req):
    suspend.after_response()
    return HttpResponse('suspending!')

@after_response.enable
def suspend():
    call(['systemctl', 'suspend'])
