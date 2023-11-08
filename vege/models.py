from django.db import models

# Create your models here.
class RecipeName(models.Model):
    recipe_name = models.CharField(max_length=50)
    recipe_desciption = models.TextField(max_length=500)
    recipe_image = models.ImageField(upload_to="receipe")