from django.shortcuts import render
from django.http import HttpResponse
from .forms import LoginForm,UserRegistrationForm,user_typeForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect 
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import user_type

def user_login(request):
    form=LoginForm()
    if request.method=="POST":
        form=LoginForm(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            user=authenticate(request,username=cd['username'],password=cd['password'])
            if user is not None:
                if user.is_active:
                   login(request,user)
                   type_obj=user_type.objects.get(user=user)
                   if user.is_authenticated and type_obj.is_doctor:
                       return redirect('/doctor/')
                   #return redirect('/dashboard/')
                   elif user.is_authenticated and type_obj.is_patient:
                        return redirect('/patient/')
                else:
                   return HttpResponse('Disabled account')
            else:
                return HttpResponse('invalid account')
    else:
           form=LoginForm()
    context={'form':form}
    return render(request,'project100app/user_login.html',context)
def user_logout(request):
     logout(request)
     return render(request,'project100app/user_logout.html')
     #messages.success(request,'You have been logged out ')


def UserRegistration(request):
    form=UserRegistrationForm()
    user_type_form=user_typeForm()
    if request.method=='POST':
        form=UserRegistrationForm(request.POST)
        user_type_form=user_typeForm(request.POST)
        if form.is_valid() and user_type_form.is_valid():
            new_user=form.save(commit=False)
            new_user.set_password(form.cleaned_data['password1'])
            new_user.save()
            new_user.refresh_from_db()
            #user_type_form=user_typeForm(request.POST,instance=request.new_user)
            new_user_type=user_type_form.save(commit=False)
            new_user_type.user=new_user
            new_user_type.save()
            
            #return HttpResponse(f'Welcome {new_user.first_name} \n Accounted created successfully')
            #return redirect('/register_done/')
       
            
            return render(request,'project100app/register_done.html',{'new_user': new_user})

            
    else:
        form=UserRegistrationForm()
    context={'form':form,'user_type_form':user_type_form}
    return render(request,'project100app/UserRegistration.html',context)

def registerdone(request):
    return render(request,'project100app/register_done.html')

def dashboard(request,id):
    user=get_object_or_404(User,id=id)
    context={'user':user}
    return render(request,'project100app/dashboard.html',context)

def doctor(request):
    return render(request,'project100app/doctor.html')

def patient(request):
    return render(request,'project100app/patient.html')