from django.contrib import admin
from . models import RecipeName
# Register your models here.

@admin.register(RecipeName)

class RecipeName(admin.ModelAdmin):
    list_display = ["recipe_name", "recipe_desciption","recipe_image"]