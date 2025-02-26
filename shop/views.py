from django.shortcuts import render,redirect
from .models import Product
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .forms import CustomUserCreationForm




# Create your views here.

def home(request):
        products = Product.objects.all()
        return render (request,'home.html',{'products': products})


def cart(request):
        return render (request,'cart.html',{})

def login_user(request):
        if request.method == "POST":
                username = request.POST['username']
                password = request.POST['password']
                user = authenticate(request,username=username,password=password)
                if user is not None:
                        login(request,user)
                        messages.success(request,('you are log in well come back'))
                        return redirect('home')
                else:
                        messages.success(request,('oh error!'))
                        return redirect ('login')
        else:
                return render(request,'login.html',{})




def logout_user(request):
        logout(request)
        messages.success(request,("you logout"))
        return redirect('home')

def signup_user(request):
        if request.method == 'POST':
                form = CustomUserCreationForm(request.POST)
                if form.is_valid():
                        user = form.save(commit=False)
                        user.email = form.cleaned_data['email']  # ذخیره ایمیل
                        user.save()
                        messages.success(request, f'حساب کاربری {user.username} با موفقیت ساخته شد!')
                        return redirect('login')
                else:
                        messages.error(request, 'خطا در ثبت نام! لطفا اطلاعات را بررسی کنید.')
        else:
                form = CustomUserCreationForm()
        return render(request, 'signup.html', {'form': form})
