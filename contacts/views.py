from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from contacts.models import Phone
from contacts.forms import PhoneForm
from django.core.exceptions import ValidationError
from contacts.forms import UserRegistratonForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout,authenticate
# # Create your views here.
def Home(request):
    return render(request,'contacts/home.html')
@login_required
def display(request):
    data=Phone.objects.all()
    return render(request,'contacts/display.html',{'data':data})
@login_required
def createcontact(request):
    form=PhoneForm()
    if request.method=='POST':
        form=PhoneForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('contacts:display')
        else:
            return render(request,'contacts/create.html',{'form':form})

    return render(request,'contacts/create.html',{'form':form})
@login_required
def update(request,id):
    data=Phone.objects.get(id=id)
    form=PhoneForm(instance=data)
    if request.method=='POST':
        form=PhoneForm(request.POST,request.FILES,instance=data)
        if form.is_valid():
            form.save()
            return redirect('contacts:display')
    return render(request,'contacts/update.html',{'form':form})
@login_required
def delete(request,id):
    data=Phone.objects.get(id=id)
    data.delete()
    return redirect('contacts:display')
@login_required
def Search(request):
    if request.method=='GET':
        return render(request,'contacts/home.html')
    else:
        d=request.POST.get('name')
        name=get_object_or_404(phone,name=d)
        if not name:
            return ValidationError('name doest not exit')
        
        return render(request,'contacts/search.html',{'data':name})
    
#Authentication and authorization
def usersignup(request):
    form=UserRegistratonForm()
    if request.method=='POST':
        form=UserRegistratonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            return render(request,'registration/signup.html',{'form':form}) 

    return render(request,'registration/signup.html',{'form':form}) 

def Userlogin(request):
    name=request.POST.get('uname')
    password=request.POST.get('password')
    user=authenticate(request,username=name,password=password)
    if user!=None:
        login(request,user)
        return redirect('/')
    return render(request,'registration/login.html')

def userlogout(request):
    logout(request)
    return redirect('contacts:login')