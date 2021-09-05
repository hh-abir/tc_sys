from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.Login, name='login' ),
    path("register/", views.Register, name='register' ),
    path("logout/", views.Logout, name='logout' ),
    path("main-dashboard/", views.Dashboard, name='dashboard' ),
]