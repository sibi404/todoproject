from django.contrib.auth import authenticate
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User,auth
from django.contrib import messages

# Create your views here.



def userAuth(user_name,ps_word):
    user = authenticate(username = user_name,password = ps_word)
    if user is not None:
        return True
    else:
        return False


def accountLogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = username,password = password)
        if user is not None:
            print("GRANTED")
            auth.login(request,user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('/')
        else:
            print("DENIED")
            messages.info(request,"invalid usrname or password!!!")
            return redirect('login')
    else:
        return render(request,'login.html')

def registration(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password1']
        try:
            user = User.objects.create_user(
                username = username,
                password = password,
                first_name = first_name,
                last_name = last_name,
                email = email)
        except:
            messages.info(request,"Username already exist")
            return redirect('registration')    
        user.save()
        return redirect('/')
    else:
        return render(request,'registration.html')

def logout(request):
    auth.logout(request)
    print("logged out")
    return redirect('/')