from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.urls import reverse
from .forms import RegistrationForm,UserEditForm,ProfileEditForm,UserLoginForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login
from django.http import HttpResponseRedirect,HttpResponse
from .models import Profile
# Create your views here.

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'Account has been created successfully!')
            return redirect('login')
        else:
            messages.error(request,f'There was an error creating your account')
    else:
        form = RegistrationForm()
    return render(request,'user/register.html',{'form':form})

@login_required
def profile(request):

    if request.method == 'POST':
        u_edit_form = UserEditForm(request.POST,instance=request.user)
        p_edit_form = ProfileEditForm(request.POST,request.FILES,instance=request.user.profile)
        if u_edit_form.is_valid() and p_edit_form.is_valid():
            u_edit_form.save()
            p_edit_form.save()
            messages.success(request,f'Profile Updated successfully')
            return redirect('profile')
        else:
            messages.error(request,f'There was an error updating your profile')
    else:
        u_edit_form = UserEditForm(instance=request.user)
        p_edit_form = ProfileEditForm(instance=request.user.profile)
    context = {'u_edit_form':u_edit_form,'p_edit_form':p_edit_form}
    return render(request,'user/profile.html',context)

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request,username=username,password=password)
            if user:
                if user.is_active:
                    login(request,user)
                    return HttpResponseRedirect(reverse('post-list'))

            else:
                messages.error(request,f'User does not exist')
    else:
        form = UserLoginForm()
    context={
        'form':form
    }
    return render(request,'user/login.html',context)
