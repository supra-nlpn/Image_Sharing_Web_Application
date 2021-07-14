# from django.contrib.auth.models import User
from django import forms
from django.forms.fields import Field
from .models import Image, User, Comment
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm

class Signup(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        "class":"form-control my-2","placeholder": "Enter Password"
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        "class":"form-control my-2","placeholder": "Confirm Password"
    }))
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username','userpic']
        labels = {'urerpic': 'proflie pic'}
        widgets = {
            "username":forms.TextInput(attrs={
                "class":"form-control my-2",
                "placeholder":"Enter Username",
            }),
            "first_name":forms.TextInput(attrs={
                "class":"form-control my-2",
                "placeholder":"Enter Firstname",
            }),
            "last_name":forms.TextInput(attrs={
                "class":"form-control my-2",
                "placeholder":"Enter Lastname",
            }),
            "email":forms.EmailInput(attrs={
                "class":"form-control my-2",
                "placeholder":"Enter Email",
            }),
            "userpic": forms.FileInput(),
        }

class ImageForm(forms.ModelForm):
 class Meta:
  model = Image
  fields = ['photo','caption']
  widgets = {
      "caption":forms.TextInput(attrs={
                "class":"form-control my-2",
                "placeholder":"Add Caption",
            }),
  }

class PfupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','first_name', 'last_name', 'email', 'userpic']
        labels = {"urerpic": "proflie pic"}
        widgets = {
            "username":forms.TextInput(attrs={
                "class":"form-control my-2",
                "placeholder":"Enter Username",
                "readonly": True,
            }),
            "first_name":forms.TextInput(attrs={
                "class":"form-control my-2",
                "placeholder":"Enter Firstname",
            }),
            "last_name":forms.TextInput(attrs={
                "class":"form-control my-2",
                "placeholder":"Enter Lastname",
            }),
            "email":forms.EmailInput(attrs={
                "class":"form-control my-2",
                "placeholder":"Enter Email",
            }),
            "userpic": forms.FileInput(attrs=
            {"class": "my-2"}),
        }
        
class Chgepwd(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={
        "class":"form-control my-2","placeholder": "Enter Old Password"
    }))
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        "class":"form-control my-2","placeholder": "Enter New Password"
    }))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        "class":"form-control my-2","placeholder": "Confirm New Password"
    }))
    class Meta:
        model = User
        fields =  ["old_password","new_password1","new_password2"]


class CapEdit(forms.ModelForm):
    class Meta:
        model = Image
        fields = ["caption"]
        widgets = {
        "caption":forms.TextInput(attrs={
                "class":"form-control my-2",
                "placeholder":"Add Caption",
            }),
  }