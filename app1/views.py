from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def homePage(request):
  return render(request,"home.html")

def signupPage(request):
  if request.method=="POST":
     uname = request.POST.get("username")
     email = request.POST.get("email")
     pass1 = request.POST.get("password1")
     pass2 = request.POST.get("password2")
     if pass1==pass2:
       my_user = User.objects.create_user(uname,email,pass1)
       my_user.save()
       return redirect("login")
     else:
       return HttpResponse("password and confirm password are not matched!")
       
  return render(request,"signup.html")

def loginPage(request):
    if request.method=="POST":
      usname = request.POST.get("username")
      passw = request.POST.get("pass")

      user = authenticate(request,username=usname,password=passw)
      if user is not None:
        login(request,user)
        return redirect("home")
      else:
        return HttpResponse("username or password is incorrect!")


    return render(request,"login.html")

def logoutPage(request):
    logout(request)
    return redirect("login")
