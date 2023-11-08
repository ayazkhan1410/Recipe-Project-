from django.shortcuts import render, redirect
from . models import *
from django.http import HttpResponse

# Create your views here.

def recepies(request):
    
    if request.method == "POST":
        # taking data from front-end
        data = request.POST
        
        recipe_image = request.FILES.get("recipe_image")
        recipe_name = data.get("recipe_name")
        recipe_desciption = data.get("recipe_desciption")
        
        # printing data for debugging
        # print(recipe_name, recipe_desciption, recipe_image)
        
        RecipeName.objects.create(recipe_name=recipe_name, recipe_desciption=recipe_desciption, recipe_image=recipe_image)
         
        return redirect("/recepies")
    
    queryset = RecipeName.objects.all()
    context = {'recipes':queryset}
    
    return render(request, "vege/index.html",context)

def delete(request, id):
   obj = RecipeName.objects.get(id=id)
   obj.delete()
   return redirect("/recepies")
   