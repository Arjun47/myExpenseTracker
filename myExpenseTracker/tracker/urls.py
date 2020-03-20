from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('exTable', views.extable, name="exTable"),
    path('login', views.Dologin, name="login"),
    path('logout', views.Dologout, name="logout"),
    path('register', views.register, name="register")
]