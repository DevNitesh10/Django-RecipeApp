from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login/') #requires login
# Create your views here.
def receipes(request):
    if request.method == "POST":
        data = request.POST
        receipe_name = data.get('receipe_name')
        receipe_description = data.get('receipe_description')
        receipe_image = request.FILES.get('receipe_image')

        Receipe.objects.create(
            receipe_name = receipe_name,
            receipe_description = receipe_description,
            receipe_image = receipe_image
        )
        return redirect('/receipes/')
    querySet = Receipe.objects.all() #objects is Manager here by default
    
    if request.GET.get('search'):
        querySet = querySet.filter(receipe_name__icontains = request.GET.get('search'))

    context = {'receipes' : querySet}
    return render(request, 'receipes.html', context)

# Views for Updating Reciepe
def update_receipe(request, id):
    querySet = Receipe.objects.get(id = id)

    if request.method == "POST":
        data = request.POST
        receipe_name = data.get('receipe_name')
        receipe_description = data.get('receipe_description')
        receipe_image = request.FILES.get('receipe_image')

        querySet.receipe_name = receipe_name
        querySet.receipe_description = receipe_description

        if receipe_image:
            querySet.receipe_image = receipe_image

        querySet.save()
        return redirect('/receipes/')

    context = {'receipe' : querySet}
    return render(request, 'update-receipes.html', context)
    
# Views for Deleting Reciepe
def delete_receipe(request, id):
    querySet = Receipe.objects.get(id = id)
    querySet.delete()
    return redirect('/receipes/')

# Views for Login page
def login_page(request):
    if request.method == "POST":
        username    = request.POST.get("username")
        password    =  request.POST.get("password")

        if not User.objects.filter(username = username).exists():
            messages.info(request, "Invalid Username!")
            return redirect("/login/")
        
        user = authenticate(username = username, password = password)

        if user is None:
            messages.info(request, "Invalid Username or Password!")
            return redirect("/login/")
        
        else:
            login(request, user)
            return redirect("/receipes/")

    return render(request, 'login.html')

def logout_page(request):
    logout(request)
    return redirect("/login/")

# Views for Register Page
def register_page(request):
    if request.method == "POST":
        first_name  = request.POST.get("first_name")
        last_name   = request.POST.get("last_name")
        username    = request.POST.get("username")
        password    =  request.POST.get("password")

        user = User.objects.filter(username = username)
        if user.exists():
            messages.info(request, "Username already exists!!!")
            return redirect('/register/')

        user = User.objects.create(
            first_name = first_name,
            last_name = last_name,
            username = username,
        )
        user.set_password(password)
        user.save()
        messages.info(request, "Account Created Successfully!")
        return redirect("/register/")

    return render(request, 'register.html')

