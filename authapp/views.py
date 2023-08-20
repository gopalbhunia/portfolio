from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout


# Create your views here.
def signup(request):
    if request.method == "POST":
        get_email =request.POST.get('email')
        get_password =request.POST.get('pass1')
        get_confirm_password =request.POST.get('pass2')
        if get_password != get_confirm_password:
            messages.info(request,'Password is not matching')
            return redirect('/auth/signup/')

        try:
            if User.objects.get(username=get_email):
                messages.warning(request,"This email is allready taken")
                return redirect('/auth/signup/')
        except Exception as identifier:
            pass
        myuser = User.objects.create_user(get_email,get_email,get_password)
        myuser.save()
        messages.success(request,'User is created successfully please Login')
        return redirect('/auth/login/')
    
    return render(request,'signup.html')

def handleLogin(request):
    if request.method == "POST":
        get_email =request.POST.get('email')
        get_password =request.POST.get('pass1')
        myuser = authenticate(username=get_email,password=get_password)
        if myuser is not None:
            login(request,myuser)
            messages.success(request,"Login Success")
            return redirect('/home')
        else:
            messages.error(request,"Invalid Details")
    return render(request,'login.html')

def handleLogout(request):
    logout(request)
    messages.success(request,"Logout Successfully")
    return render(request,'login.html')
