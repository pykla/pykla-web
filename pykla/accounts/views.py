from django.shortcuts import render, redirect
from.forms import RegForm, EditProfile
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


# index view
def index(request):
    return render(request, 'base.html')

#registration view
def reg(request):
    if request.method == 'POST':
        form = RegForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = RegForm()

    args = {'form': form}
    return render(request, 'acc/reg.html', args)

# view for editing user profile
@login_required
def profile(request):
    pro = {'user': request.user}
    return render(request, 'acc/profile.html', pro)

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfile(request.POST, instance = request.user)

        if form.is_valid():
            form.save()
            return redirect('profile')

    else:
        form = EditProfile(instance=request.user)
    args = {'form' : form}

    return render(request, 'acc/edit_pro.html', args)


# view for editing passsword
@login_required
def edit_pass(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user = request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('profile')
        else:
            return redirect('edit_pass')

    else:
        form = PasswordChangeForm(user=request.user)

        args={'form':form}
        return render(request, 'acc/edit_pass.html', args)