from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import turicreate

from .forms import PredictForm

def index(request) :
    form = PredictForm(request.POST or None)
    if request.method == "POST" :
        message = request.POST.get('message')
        print(message)
        result = predictValue(message)
        print(result)
    
    form = PredictForm()
    return render(request,"home.html",{"title":"Home","form":form})

# Changes made here
def predictValue(s):
    data = turicreate.SFrame.read_csv('SMSSpamCollection', header=False, delimiter='\t', quote_char='\0')
    data = data.rename({'X1': 'label', 'X2': 'text'})
    train, test = data.random_split(0.8)
    model = turicreate.text_classifier.create(train, 'label', features=['text'], max_iterations=10000)
    x = turicreate.SFrame({'text':[s]})
    return model.predict(x)
