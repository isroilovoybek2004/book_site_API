from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from django.views import View
from .models import CustomUser
from .forms import CustomUserCreateForm,CustomUserUpdateForm
from django.contrib.auth.forms import AuthenticationForm


# Create your views here.
class UserRegisterView(View):
    def get(self, request):
        create_form = CustomUserCreateForm()
        context = {
            'form': create_form
        }
        return render(request, 'users/register.html', context)

    def post(self, request):
        create_form = CustomUserCreateForm(request.POST)
        create_form.is_valid()
        create_form.save()
        return redirect('users:login')


        # username = request.POST['username']
        # first_name = request.POST['first_name']
        # last_name = request.POST['last_name']
        # email = request.POST['email']
        # password = request.POST['password']
        #
        # user = CustomUser.objects.create(
        #     username=username,
        #     first_name=first_name,
        #     last_name=last_name,
        #     email=email,
        #     password=password
        #
        # )
        # user.set_password(password)
        # user.save()


class CustomUserLogin(View):
    def get(self,request):
        login_form = AuthenticationForm
        # create_form = CustomUserCreateForm()
        context = {
            'form': login_form
        }
        return render(request, 'users/login.html', context)

    def post(self,request):
        data = AuthenticationForm(data=request.POST)
        data.is_valid()
        user = data.get_user()
        login(request, user)
        return redirect('home')


class LogoutView(View):
    def get(self, request):
        logout(request)
        return render(request,"home.html")


class ProfileView(View):
    def get(self,request):
        context = {
            'user':request.user
        }
        return render(request,'users/profile.html',context=context)


class ProfileUpdateView(View):
    def get(self,request):
        update_form = CustomUserUpdateForm(instance=request.user)
        context = {
            'update_form': update_form
        }
        return render(request, 'users/profile_update.html', context=context)

    def post(self, request):
        update_form = CustomUserUpdateForm(
            instance=request.user,
            data=request.POST,
            files=request.FILES
        )
        if update_form.is_valid():
            update_form.save()
            return redirect('users:profile')
        else:
            return render(request, 'users/profile_update,html', {'update_form':update_form})