from django.db import models

# Create your models here.
class RecipeName(models.Model):
    recipe_name = models.CharField(max_length=50)
    recipe_desciption = models.TextField(max_length=1000)
    recipe_image = models.ImageField(upload_to="recepies")
    
    def __str__(self):
        return self.recipe_name