from django.shortcuts import render
from django.http import JsonResponse
from .models import Contact

def home(request):
    if request.method =="POST":
        name_form = request.POST['name']
        email_form = request.POST['email']
        subject_form = request.POST['subject']
        message_form = request.POST['message']
        Contact.objects.create(name=name_form,email=email_form,subject=subject_form,message=message_form)

        return render(request, 'home.html',{})
        
        
    else:
        
        return render(request, 'home.html',{})

    return render(request, 'home.html', {})


