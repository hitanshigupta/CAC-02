from django.shortcuts import render, redirect
from cadmin.models import Streets
from cadmin.models import Contact_Form
from cadmin.models import UserType
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


def index(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        ph_no = request.POST['ph_no']
        msg = request.POST['msg']
        contact = Contact_Form.objects.create(name=name, email=email, ph_no=ph_no, message=msg)
        contact.save()
        return redirect('index')
    streets = Streets.objects.filter(Street_status=1)
    return render(request , 'Users/main/index.html', {'street': streets})


def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_active:
            login(request, user)
            return redirect('index')
        else:
            msg = "Wrong Credentaials! Please try again!"
            return render(request, 'main/signin.html', {'msg': msg})
    return render(request, 'main/signin.html')


def user_registration(request):

    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                msg = "Username already exists. Please try another one!"
                return render(request, 'main/signup.html', {'msg':msg})
            else:
                user = User.objects.create_user(first_name=first_name, last_name=last_name, email=email, username=username)
                user.set_password(password)
                user.save()
                usertype = UserType.objects.create(user=user, usertype='User')
                usertype.save()
                return redirect('user_login')
        else:
            msg = "Passwords do not match. Please try again!"
            return render(request, 'main/signup.html', {'msg':msg})
    return render(request, 'main/signup.html')


def user_logout(request):
    logout(request)
    return redirect('user_login')


def redirect_page(request):
    return render(request, 'Users/main/redirect.html')





