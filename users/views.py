from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def register(request):
    if request.method=='POST':
        #gettin data from form 
        form=UserCreationForm(request.POST)
        #check for validation
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,f'Welcome {username}, your account is created')
            return redirect('users:login')
    else:
        form=UserCreationForm()
    return render(request,'users/register.html',{'form':form})



@login_required
def profile(request):
     
     return render(request,'users/profile.html')
