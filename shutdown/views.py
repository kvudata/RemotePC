from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from subprocess import call

import after_response
import platform

# Create your views here.

def show_controls(req):
    return render(req, 'shutdown/controls.html')

def handle_suspend_req(req):
    suspend.after_response()
    return render(req, 'shutdown/controls.html', {'msg': 'suspending'})

@after_response.enable
def suspend():
    if platform.system() == 'Windows':
        call(['shutdown', '/h'])
    call(['systemctl', 'suspend'])
