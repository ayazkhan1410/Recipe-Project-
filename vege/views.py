from django.shortcuts import render, redirect
from . models import *
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url="/recepies/login")
def recepies(request):
    
    if request.method == "POST":
        # taking data from front-end
        data = request.POST
        
        recipe_image = request.FILES.get("recipe_image")
        recipe_name = data.get("recipe_name")
        recipe_desciption = data.get("recipe_desciption")
               
        RecipeName.objects.create(recipe_name=recipe_name, recipe_desciption=recipe_desciption, recipe_image=recipe_image)
         
        return redirect("/recepies")
    
    queryset = RecipeName.objects.all()
    
    if request.GET.get('search'):
        queryset = queryset.filter(recipe_name__icontains=request.GET.get('search'))
    
    context = {'recipes':queryset}
    return render(request, "vege/index.html",context)

@login_required(login_url="/recepies/login")
def update(request, id):
    try:
        # Fetch the specific recipe to update
        recipe = RecipeName.objects.get(id=id)
    except RecipeName.DoesNotExist:
        return HttpResponse("Recipe does not exist")  # Handle the case where the recipe doesn't exist

    if request.method == "POST":
        data = request.POST
        recipe_name = data.get("recipe_name")
        recipe_description = data.get("recipe_description")
        recipe_image = request.FILES.get("recipe_image")

        recipe.recipe_name = recipe_name
        recipe.recipe_description = recipe_description

        if recipe_image:
            recipe.recipe_image = recipe_image

        recipe.save()

        return redirect("/recepies")  # Redirect to the "recepies" page after updating

    context = {'recipe': recipe}
    return render(request, "vege/update.html", context)

@login_required(login_url="/recepies/login")
def delete(request, id):
   obj = RecipeName.objects.get(id=id)
   obj.delete()
   return redirect("/recepies")
   
   
def register(request):
    
    if request.method == "POST":
        data = request.POST
        first_name = data.get("Firstname")
        last_name = data.get("Lastname")
        username = data.get("Username")
        password = data.get("Password")
        
        user = User.objects.filter(username=username)
        
        if user.exists():
            messages.info(request, "User already exists.")
            return redirect("/recepies/register")
        else:
            user = User.objects.create(first_name=first_name,last_name=last_name,username=username)
            user.set_password(password)
            user.save()
            messages.info(request, "Account created successfully.")
            return redirect("/recepies/register")
            
    return render(request, "vege/register.html")


def login_page(request):
    
    if request.method == "POST":
        data = request.POST
        username = data.get("username")
        password = data.get("password")
        
        if not User.objects.filter(username = username).exists():
            messages.info(request,"User does not exist, Please Create account")
            return redirect("/recepies/login")
        
        user = authenticate(username=username, password=password)
        
        if user is None:
            messages.error(request, "Wrong Password")
            return redirect("/recepies/login")
        else:
            login(request,user)
            return redirect("/recepies")
            
    return render(request, "vege/login.html")

def log_out(request):
    
    logout(request)
    return redirect("/recepies/login")