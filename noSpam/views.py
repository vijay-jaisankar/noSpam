from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect


def index(request) :
    if request.method == "POST" :
        print(request.POST.get('textarea'))
        message = request.POST.get('textarea')
        
    return render(request,"home.html",{"title":"Home"})
