from django.shortcuts import render
from app.models import contact_form

def homepage(request):
    return render(request,"index.html")
def aboutus(request):
    return render(request,"#about")
def course(request):
    return render(request,"#course")
def blog(request):
    return render(request,"#blog")
 
def contact(request):
    return render(request,"#contact")

def contactform(request):
    stud = contact_form.objects.all()
    if request.method == "POST":
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        Message = request.POST.get('Message')
        applydata = contact_form(fname=fname ,lname=lname ,phone=phone, email=email, Message=Message)
        applydata.save()
       

    return render(request, "index.html", {'stu':stud})
 


 

