from django.urls import path
from . import views

urlpatterns = [
    path('signup' , views.signup, name="signup"),
    path('signin' , views.signin, name="signin"),
    path('signout' , views.signout, name="signout"),
    path('delete/<str:user>' , views.delete_user, name="delete-user")

]
