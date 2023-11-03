from django.shortcuts import render
from menu.models import Feedback

# Create your views here.


def index(request):
    return render(request,'index.html')

def user_feedback(request):
    if request.method == 'POST':
        name = request.POST['name']
        text= request.POST['text']
        data = Feedback(name=name,text=text)
        data.save()

    data=Feedback.objects.all()
    dict = {
        'allfeedback': data,
       
    }
    return render(request,'user_feedback.html',dict)
    

