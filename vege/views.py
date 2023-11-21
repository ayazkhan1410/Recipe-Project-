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
               
        RecipeName.objects.create(recipe_name=recipe_name, recipe_desciption=recipe_desciption, recipe_image=recipe_image)
         
        return redirect("/recepies")
    
    queryset = RecipeName.objects.all()
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
   