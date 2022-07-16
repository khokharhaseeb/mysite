from django.shortcuts import render,HttpResponse
from .models import contact_message,medical_billing,dental_billing,credentialing

# Create your views here.
# Create your views here.
def home(request):
    return render(request, 'hom/index.html')
    
def contactus(request):
    return render(request, 'hom/contact.html')


def aboutus(request):
 
    return render(request, 'hom/about-us.html')


def medical(request):
    return render(request, 'hom/medical-billing.html')


def dental(request):
    return render(request, 'hom/dental-billing-services.html')

def credential(request):
    return render(request, 'hom/credentialing.html')


def contact_submit(request):

    name = request.POST.get('name')
    email = request.POST.get('email')
    subject = request.POST.get('subject')
    message = request.POST.get('message')
    cm = contact_message(Name=name, Email=email, Subject=subject, Message=message)
    
    cm.save()

    return render(request, 'hom/contact.html')


def medical_submit(request):
    
    name = request.POST.get('name')
    email = request.POST.get('email')
    subject = request.POST.get('subject')
    message = request.POST.get('message')
    cm = medical_billing(Name=name, Email=email, Subject=subject, Message=message)
    
    cm.save()

    return render(request, 'hom/medical-billing.html')


def dental_submit(request):
    
    name = request.POST.get('name')
    email = request.POST.get('email')
    subject = request.POST.get('subject')
    message = request.POST.get('message')
    cm = dental_billing(Name=name, Email=email, Subject=subject, Message=message)
    
    cm.save()

    return render(request, 'hom/dental-billing-services.html')


def credentialing_submit(request):
    
    name = request.POST.get('name')
    email = request.POST.get('email')
    subject = request.POST.get('subject')
    message = request.POST.get('message')
    cm = credential(Name=name, Email=email, Subject=subject, Message=message)
    
    cm.save()

    return render(request, 'hom/credentialing.html')