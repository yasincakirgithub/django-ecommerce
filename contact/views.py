from django.shortcuts import render,redirect
from django.urls import reverse
from contact.forms import ContactForm
from django.contrib import messages
# Create your views here.

def ContactPage(request):

    if request.method == "POST":
        form = ContactForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been received')
            return redirect(reverse("contact-page"))
    else:
        form = ContactForm()

    return render(request,'contact/index.html',context={ 'form':form })