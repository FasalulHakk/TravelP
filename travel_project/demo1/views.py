from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method == 'POST':
        user1 = request.POST['username']
        password = request.POST['password']
        user2 = auth.authenticate(username=user1, password=password)

        if user2 is not None:
            auth.login(request, user2)
            return redirect('/')
        else:
            messages.info(request, 'invalid')
            return redirect('login')

    return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        name1 = request.POST['first_name']
        name2 = request.POST['last_name']
        mail = request.POST['email']
        password = request.POST['password']
        password1 = request.POST['password1']
        if password == password1:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'username is already taken')
                return redirect('register')
            elif User.objects.filter(email=mail).exists():
                messages.info(request, 'email is already taken')
                return redirect('register')

            else:
                user = User.objects.create_user(username=username, first_name=name1, last_name=name2, email=mail,
                                                password=password)
                user.save()
                return redirect('login')  # after user creation, go to login page

        else:
            messages.info(request, ' password is not matching')
            return redirect('register')

        return redirect('/')  # after user creation go to login page,so here no need to go back to home page

    return render(request, 'index2.html')
