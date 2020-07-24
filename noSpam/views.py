from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .forms import PredictForm

def index(request) :
    form = PredictForm(request.POST or None)
    if request.method == "POST" :
        #print(request.POST.get('textarea'))
        #message = request.POST.get('textarea')
        # if form.is_valid() :
        #     return HttpResponseRedirect('/thanks/')
        message = request.POST.get('message')
        print(message)
        
    return render(request,"home.html",{"title":"Home","form":form})
