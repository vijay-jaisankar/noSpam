from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .forms import PredictForm

def index(request) :
    form = PredictForm(request.POST or None)
    if request.method == "POST" :
        message = request.POST.get('message')
        print(message)
    
    form = PredictForm()
    return render(request,"home.html",{"title":"Home","form":form})
