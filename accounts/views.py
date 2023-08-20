from django.shortcuts import redirect, render
from .models import *       #new
from django.contrib import messages
from django.contrib.messages import constants
from accounts.models import Contact,Blog

# Create your views here.
def home(request):
    skills = skillupdate.objects.all()
    context ={"skills":skills}
    return render(request,'home.html',context)
    

def about(request):
    posts = skillupdate.objects.all()
    context ={"posts":posts}
    return render(request,'about.html',context)

def project(request):
    posts = Project.objects.all()
    context = {"posts":posts}
    return render(request, 'projects.html',context)


def blog(request):
    posts = Blog.objects.all()
    context = {"posts":posts}
    return render(request, 'blog.html',context)

def contact(request):
    if request.method == "POST":
        fname = request.POST.get('name') 
        femail = request.POST.get('email') 
        fphoneno = request.POST.get('num')
        fdesc = request.POST.get('desc')
        
        query = Contact(name=fname,email=femail,phonenumber=fphoneno,description=fdesc)
        query.save()
        messages.success(request,'Thanks for contact me.I will reply soon')
        
        return redirect('/contact')
    return render(request,'contact.html')


#----Blog details page views-----
def detail(request, id):
    var = Blog.objects.get(pk=id)
    return render(request, 'detail.html',{'Blog':var})

#-----Projects Details page views------
def pdetail(request, id):
    varr =  Project.objects.get(pk = id)
    return render(request, 'pdetail.html',{'Project':varr})