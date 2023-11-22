from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class RecipeName(models.Model):
    
    # Establishes a connection between 'this data' and a 'User' 
    # If the 'User' is deleted, keeps the connection but sets 'this data' to empty
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    
    recipe_name = models.CharField(max_length=50)
    recipe_desciption = models.TextField(max_length=1000)
    recipe_image = models.ImageField(upload_to="recepies")
    
    def __str__(self):
        return self.recipe_name