from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('exTable', views.extable, name="exTable"),
    path('login', views.Dologin, name="login"),
    path('logout', views.Dologout, name="logout"),
    path('register', views.register, name="register"),
    path('alltransactions/', views.TransactionAV.as_view(), name="transaction-list"),
    path('categories/', views.CategoryAV.as_view(), name="categories"),
    path('users/', views.UserAV.as_view(), name="users")
]
