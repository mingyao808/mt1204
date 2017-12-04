from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
# Create your views here.
def sayhello(request):
    return HttpResponse('ABC1204');
def hello(request,username):
    now=datetime.now()
    return render(request,"hello.html",locals())
