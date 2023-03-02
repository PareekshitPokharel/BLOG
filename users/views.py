from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordResetView
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _


# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'The username {username} has been successfully registerd!')
            return redirect ('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form':form})


@login_required(login_url='login')
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(
                request, f'The form has been updated successfully!')
            return redirect('profile')
            
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    
    context = {
        'u_form':u_form,
        'p_form':p_form
    }
    return render (request, 'users/profile.html',context)


class PasswordReset(PasswordResetView):
    
    def post(self, request, *args, **kwargs):
            form = self.get_form()
            if form.is_valid():
                clean_data = form.cleaned_data.get('email')
                if clean_data == self.request.user.email:
                    return self.form_valid(form)
                else:
                    messages.error(request,'Invalid email address')
                    return self.form_invalid(form)
                


            


   
        

