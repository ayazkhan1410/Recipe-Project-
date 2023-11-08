from django.shortcuts import render

# Create your views here.

def recepies(request):
    
    if request.method == "POST":
        data = request.POST
        recipe_name = data.get("recipe_name")
        recipe_desciption = data.get("recipe_desciption")
        print(recipe_name, recipe_desciption)
        
    return render(request, "vege/index.html")