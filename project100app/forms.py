from django import forms 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm,TextInput,EmailInput,PasswordInput,Textarea,FileInput,ChoiceField
from .models import user_type


class LoginForm(forms.Form):
    username=forms.CharField(max_length=50,widget=forms.TextInput(attrs={'placeholder':'Username or Email'}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'password'}))

class UserRegistrationForm(UserCreationForm):
    email=forms.EmailField(max_length=50,help_text='Required',widget=forms.EmailInput(attrs={'placeholder':'email'}))
    password1=forms.CharField(max_length=50,widget=forms.PasswordInput(attrs={'placeholder':'password'}))
    password2=forms.CharField(max_length=50,widget=forms.PasswordInput(attrs={'placeholder':'Re Enter password'}))
    #extra_field=forms.CharField(max_length=50,required=True)
    class Meta:
        model=User
        fields=['username','email','password1','password2','first_name','last_name',]
        widgets={
            'username':TextInput(attrs={'placeholder':'username'}),
            'first_name':TextInput(attrs={'placeholder':'First Name'}),
            'last_name':TextInput(attrs={'placeholder':'Last Name'}),
        }

        
class user_typeForm(forms.ModelForm):
    class Meta:
        model=user_type
        fields=['photo','adress','is_doctor','is_patient']
        widget={
            'doctor_or_patient':ChoiceField(required=True)
        }