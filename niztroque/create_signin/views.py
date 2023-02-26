from django.shortcuts import render,redirect
from django.contrib.auth.forms import  UserCreationForm
from django.contrib import messages
from .form import UserRegisterForm

# Create your views here.
def user_login(request):
        if request.method == 'POST':
                print('Hello')
                form = UserRegisterForm(request.POST)
                if form.is_valid():
                        form.save()
                        username=form.cleaned_data.get('username')
                        messages.success(request,f'Account has been created . You can now log in ')
                        return redirect('login')

        else:
                form = UserRegisterForm()
        return render(request,'create_signin/create_signin.html',{'form':form})
