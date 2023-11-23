from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.recepies,name="recepies"), 
    path("delete/<int:id>", views.delete,name="delete"),
    path("update/<int:id>", views.update,name="update"),
    path("register",views.register,name="register"),
    path("login",views.login_page,name="login"),
    path("logout",views.log_out,name="logout")
]
