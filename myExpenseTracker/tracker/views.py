from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, auth
from django.contrib import messages
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Expense, Categories
from .serializers import TransactionSerializer, CategorySerializer, UserSerializer

# Create your views here.


class TransactionAV(APIView):

    def get(self, request):
        expenses = Expense.objects.all()
        serializer = TransactionSerializer(expenses, many=True)
        return Response(serializer.data)


class CategoryAV(APIView):

    def get(self, request):
        categories = Categories.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class UserAV(APIView):

    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)


def index(request):
    return render(request, 'base.html')


def extable(request):
    return render(request, 'exTable.html')


def Dologin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Wrong Credentials ')
    return render(request, 'login.html')


def Dologout(request):
    logout(request)
    return redirect('index')


def register(request):
    if request.method == 'POST':
        first_Name = request.POST['firstName']
        last_Name = request.POST['lastName']
        email1 = request.POST['email']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                print("already taken")
                return render(request, 'register.html')
            elif User.objects.filter(email=email1).exists():
                print("email taken")
                return render(request, 'register.html')
            else:
                user = User.objects.create_user(
                    username=username, email=email1, password=password1, first_name=first_Name, last_name=last_Name)
                user.save()
                print("user created")
                user = authenticate(
                    request, username=username, password=password1)
                login(request, user)
                return redirect('index')
    else:
        print("user not created")
        return render(request, 'register.html')
