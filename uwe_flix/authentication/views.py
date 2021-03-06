from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import UserUpdateForm, ProfileUpdateForm

# Create your views here.
def home(request):
	"""the homepage view"""
	context = {}
	template = 'index.html'
	return render(request,template,context)


def signup(request):
    

    if request.method == 'POST':
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        if User.objects.filter(username = username).first():
            messages.error(request, "This username is already taken")
            return redirect('home')
        

        myuser = User.objects.create_user(username, email,  pass1)
        myuser.first_name = fname
        myuser.last_name = lname

        myuser.save()
        
        messages.success(request, "Your account has been signed up.")

        return redirect('signin')

    return render(request,"signup.html")

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']
        
        user = authenticate(username=username, password=pass1)

        if user is not None:
            login(request, user)
            fname = user.first_name
            return render(request, "index.html",  { 'username': username, 'fname': fname})
        else:
            messages.error(request, "Bad Cresentials!")
            return redirect('home')
    return render(request,"signin.html")

def signout(request):
    logout(request)
    messages.success(request, "Your account has been logged out!")
    return redirect('signin')

@login_required(login_url='player_login') 
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm( request.POST, 
                                    request.FILES,
                                    instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account profile has been updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request,"userprofile.html", context)


