from django.shortcuts import render

# Create your views here.

def searchPage(request):
    return render(request,"myapp/searchPage.html")

def indexView(request):
    people_list = [
        {"name": "Ayaz", "age": 22},
        {"name": "Ali", "age": 21},
        {"name": "Affan", "age": 22},
        {"name": "Mudassir", "age": 12},
    ]
    
    text = ["Tomato","LadyFinger","Potato","Cucumber"]
    
    return render(request, "myapp/index.html", {"peoples": people_list, 'text':text})

def about(request):
    return render(request,"myapp/about.html")

def contact(request):
    return render(request,"myapp/contact.html")

def htmlforms(request):
    return render(request, "myapp/Forms.html")


