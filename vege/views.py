from django.shortcuts import render, redirect
from . models import *
from django.http import HttpResponse
from django.contrib.auth.models import User

# Create your views here.

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


def delete(request, id):
   obj = RecipeName.objects.get(id=id)
   obj.delete()
   return redirect("/recepies")
   
   
def register(request):
    
    
    
    if request.method == "POST":
        data = request.POST
        Firstname = data.get("Firstname")
        Lastname = data.get("Lastname")
        Username = data.get("Username")
        Password = data.get("Password")
        
        user = User.objects.filter(Username=Username)
        
        if user.exists():
            pass
        
        user = User.objects.create_user(first_name=Firstname, last_name=Lastname, username=Username)
        
        user.set_password(Password)
        user.save()
        
        return redirect("/recepies/register")
    
    return render(request, "vege/register.html")


def login(request):
    return render(request, "vege/login.html")