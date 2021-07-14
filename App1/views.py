from django.contrib.auth import login
from App1.models import Image, User, Comment
from django.shortcuts import render, redirect
from App1.forms import CapEdit, Chgepwd, Signup, ImageForm, PfupForm
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.models import User

# Create your views here.
@login_required
def home(request):
    a = Image.objects.all()
    return render(request, 'html/home.htm', {'q': a})

def welcome(request):
    return render(request, 'html/welcome.htm')

def signup(request):
    if request.method == 'POST':
        a = Signup(request.POST, request.FILES)
        if a.is_valid():
            a.save()
            return redirect('/login') 
    a = Signup()
    return render(request, 'html/signup.htm', {'d':a})

@login_required
def addimg(request):
    if request.method == 'POST':
        a = ImageForm(request.POST, request.FILES)
        if a.is_valid():
            c = a.save(commit=False)
            c.uid_id= request.user.id
            c.save()
            a.save()
            return redirect('/home')
    a = ImageForm()
    
    return render(request, 'html/addimg.htm', {'b': a})

@login_required
def profile(request):
    y = Image.objects.filter(uid_id= request.user.id)
    return render(request, 'html/profile.htm', {'k': y})

# @login_required
# def profupdt(request):
#     z = User.objects.get(id = request.user.id)
#     if request.method == 'POST':
#         y = PfupForm(request.POST, request.FILES, instance=z)
#         if y.is_valid():
#             y.save()
#             return redirect('/profile')
#     y = PfupForm(instance=z)
#     return render(request, 'html/profupdt.htm', {'k': y})

@login_required
def profupdt(request):
    d=User.objects.get(id=request.user.id)
    if request.method=="POST":
        pf=PfupForm(request.POST,request.FILES,instance=d)
        if pf.is_valid():
            pf.save()
            return redirect('/profile')
    pf=PfupForm(instance=d)
    return render(request,'html/profupdt.htm',{'k':pf})

@login_required
def delimg(request, m):
    y = Image.objects.get(id = m)
    r = Comment.objects.filter(imageid_id= m)
    if request.method == 'POST':
        y.delete()
        r.delete()
        return redirect('/profile')
    return render(request, 'html/delimg.htm')

@login_required
def showimg(request, m):
    y = Image.objects.get(id = m)
    z = User.objects.get(id=y.uid_id)
    q = Comment.objects.filter(imageid_id = m)
    if request.method == 'POST':
        s = request.user.username 
        h = request.POST['comment']
        obj = Comment(imageid_id = m, uname = s, comment = h)
        obj.save()
        return render(request, 'html/showimg.htm', {'k':y, 'u': z, 'a': q })
    return render(request, 'html/showimg.htm', {'k':y, 'u': z, 'a': q})

@login_required
def changepwd(request):
    if request.method == "POST":
        k = Chgepwd(user=request.user,data=request.POST)
        if k.is_valid():
            k.save()
            return redirect('/login')
    k = Chgepwd(user=request)
    return render(request,'html/changepwd.htm',{'t':k})

@login_required
def capedit(request, m):
    d = Image.objects.get(id = m)
    if request.method == 'POST':
        h = CapEdit(request.POST, instance= d)
        if h.is_valid():
            h.save()
            return redirect('/profile')
    h = CapEdit(instance=d)
    return render(request, 'html/capedit.htm', {'u':h})

@login_required
def showprofile(request, m):
    h = Image.objects.filter(uid_id = m)
    z = User.objects.get(id = m)
    return render(request, 'html/showprofile.htm', {'x': h, 'p': z})