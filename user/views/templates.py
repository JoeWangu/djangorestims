from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import views as auth_views
# from django.contrib.auth.decorators import login_required
from user.forms import UserForm, LoginForm

# Create your views here.
def user_home(request):
    title = 'Home'
    context = {
        'title': title,
    }
    return render(request, 'user/user_home.html', context)

def signup(request):
    title = 'Create User'
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('user_home')
    else:
        form = UserForm()
    context = {
        'title': title,
        'form': form,
    }
    return render(request, 'registration/signup.html', context)


def logoutView(request):
    title = 'Logged Out'
    context = {
        'title': title,
    }
    return render(request, 'registration/logout.html', context)


class MyLoginView(auth_views.LoginView):
    form_class = LoginForm