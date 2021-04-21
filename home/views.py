from django.shortcuts import render, HttpResponse,redirect
from .models import Event
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# Create your views here.

def home(request):
    allEvents = Event.objects.all()[0:4]   
    context = {'allEvents':allEvents}
    
    return render(request,'home/index.html',context)
def events(request):
    allEvents = Event.objects.all()
    context = {'allEvents':allEvents}
    return render(request,'home/Events.html',context)
    

def addEvent(request):
    if request.user.is_authenticated:     
        if request.method=="POST":
            user = request.user.username
            name = request.POST.get('name')
            performers = request.POST.get('performers')
            venue = request.POST.get('venue')
            address = request.POST.get('address')
            date = request.POST.get('date')
            time = request.POST.get('time')
            image = request.POST.get('image')
            desc = request.POST.get('desc')
            newEvent = Event(user=user,name=name,performers=performers,venue=venue,image=image,date=date,time=time,desc=desc)
            newEvent.save()
            messages.success(request,"You have successfully added event ")
            return redirect('/')

        return render(request,'home/AddEvent.html')
    else:
        return HttpResponse("User is not authentical")    

def details(request,slug):
    event = Event.objects.filter(name=slug).first()
    context = {'event':event}
    return render(request,'home/Detail.html',context)

    
    return render(request,'home/Detail.html',context)

def dashboard(request):
    if  request.user.is_authenticated:
        allEvents = Event.objects.filter(user=request.user.username)
        context = {'allEvents':allEvents}
        return render(request,'home/Dashboard.html',context)
    else:
        return HttpResponse("You are not authenticates")    

def handleLogin(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,"You have successgully logged in")
            return redirect('/')
            
        else:
            messages.error(request,"Invalid Credentials. Please try again")  
            return redirect('/login')        
    
    return render(request,'home/Login.html')

def handleSignin(request):
    if request.method== "POST":
        username = request.POST.get('username')
        email = request.POST.get("email")
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')
        if password==cpassword:
            user = User.objects.create_user(username,email,password)
            user.save()
            messages.success(request,"You have successfully registered ")
            return redirect('/login')
        else:
            messages.error(request,"Password do not match ")  
            return redirect("/register") 
      
            
    return render(request,'home/Register.html')

def handleLogout(request):
    logout(request)
    messages.success(request,"You have successfully logged out ")
    return redirect("/")

def editEvent(request,slug):
    event = Event.objects.filter(name=slug).first()
    Event.objects.filter(name=slug).delete()
    context = {'event':event}
    return render(request,'home/AddEvent.html',context)

def deleteEvent(request,slug):
    Event.objects.filter(name=slug).delete()
    messages.error(request,"You have successgully deleted a event ")
    return redirect("/dashboard")

def search(request):
    
    query = request.POST.get('query')
    events = Event.objects.filter(name__icontains=query)
    context = {"events":events,'query':query}
        
    return render(request,'home/Search.html',context)  