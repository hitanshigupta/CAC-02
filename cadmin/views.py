from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .models import staff_details
from .models import Notification
from .models import UserType
from .models import House
from .models import h_img
from .models import Streets
from .models import Contact_Form


@login_required(login_url='admin_login')
def dashboard(request):
    noti = Notification.objects.filter(is_read=False).order_by('-created_at')
    user_count = User.objects.all().count()
    staff = User.objects.filter(is_staff=True, is_superuser=False)
    staff_count = staff.count()
    student_count = User.objects.filter(is_staff=False, is_superuser=False).count()
    page = "Dashbaord"
    return render(request, 'admin/dashboard.html',
                  {'page': page, 'noti': noti, 'user_count': user_count, 'staff_count': staff_count,
                   'student_count': student_count})


def staff_dashboard(request):
    page = "Staff Dashbaord"
    return render(request, 'staff/staff_dashboard.html', {'page': page})


def hw_dashboard(request):
    page = "House Owner Dashbaord"
    return render(request, 'HouseOwner/dashboard.html', {'page': page})


### ADMIN ------------------------------------------------------------------------------------------------------------------------------------


def admin_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_active:
            userType = None
            print(UserType.objects.filter(user_id=user.id))
            if UserType.objects.filter(user_id=user.id):
                userType = UserType.objects.get(user_id=user.id)
            if user.is_superuser == True and user.is_staff == True:
                login(request, user)
                return redirect(reverse('dashboard'))
            elif user.is_staff == True and user.is_superuser == False:
                login(request, user)
                return redirect(reverse('staff_dashboard'))
            elif userType.usertype == "House Owner":
                login(request, user)
                return redirect('hw_dashboard')
        else:
            msg = "Wrong credentials. Please try again!"
            return render(request, 'main/signin.html', {'msg': msg})
    return render(request, 'main/signin.html')


def read_msg(request, msg_id):
    noti = Notification.objects.get(id=msg_id)
    noti.is_read = True
    noti.save()
    return redirect('dashboard')


def staff_login(request):
    return render(request, )


def admin_logout(request):
    logout(request)
    return redirect('admin_login')


# Staff

def create_staff(request):
    if request.method == "POST":
        first_name = request.POST.get('fname')
        last_name = request.POST.get('lname')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')
        if cpassword == password:
            if User.objects.filter(username=username).exists():
                msg = "Username already exists. Please try another one!"
                return render(request, 'admin/staff/create_staff.html', {'msg': msg})
            else:
                user = User.objects.create_user(first_name=first_name, last_name=last_name, email=email,
                                                username=username)
                user.set_password(password)
                user.is_staff = True
                user.save()
                noti = Notification.objects.create(user=user, message="New Staff Added")
                type = UserType.objects.create(user=user, usertype="Staff")
                type.save()
                noti.save()
                return redirect('admin_login')

        else:
            msg = "Passwords didn't match. please try again!"
            return render(request, 'admin/staff/create_staff.html', {'msg': msg})
    page = "Create Staff"
    return render(request, 'admin/staff/create_staff.html', {'page': page})


def staff_list(request):
    user = User.objects.filter(is_staff=True, is_superuser=False)
    noti = Notification.objects.filter(is_read=False).order_by('-created_at')
    page = "Staff List"
    return render(request, 'admin/staff/staff_list.html', {'page': page, 'user': user, 'noti': noti})


def StaffStatusChange(request, user_id):
    user = User.objects.get(id=user_id)
    if user.is_active == False:
        user.is_active = True
        user.save()
        return redirect('staff_list')
    if user.is_active == True:
        user.is_active = False
        user.save()
        return redirect('staff_list')
    return redirect('staff_list')


def edit_staff(request, staff_id):
    user = User.objects.get(id=staff_id)
    if request.method == "POST":
        user.first_name = request.POST.get('fname')
        user.last_name = request.POST.get('lname')
        user.email = request.POST.get('email')
        user.save()
        return redirect('staff_list')
    page = "Edit Staff"
    return render(request, 'admin/staff/edit_staff.html', {'user': user, 'page': page})


def staff_passwordchange(request, staff_id):
    user = User.objects.get(id=staff_id)
    if request.method == "POST":
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')
        if password == cpassword:
            user.set_password(password)
            user.save()
            return redirect('staff_list')

    return render(request, 'admin/staff/password_change.html')


# HOUSE OWNER
def hwlist(request):
    hw_user = User.objects.filter(usertype__usertype="House Owner")
    page = "House Owner's List"
    return render(request, 'admin/houseOwner/hwlist.html', {'user': hw_user, 'page': page})


def createhw(request):
    if request.method == "POST":
        username = request.POST.get('username')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')
        if cpassword == password:
            user = User.objects.create_user(first_name=fname, last_name=lname, username=username, email=email)
            user.set_password(password)
            user.save()
            user_type = UserType.objects.create(user=user, usertype="House Owner")
            user_type.save()
            return redirect('hwlist')
        else:
            msg = "Password and Comfirm Password didn't match! Please try again!"
            return render(request, 'admin/houseOwner/createhw.html', {'msg': msg})
    page = "Create House Owner"
    return render(request, 'admin/houseOwner/createhw.html', {'page': page})


# Users

def users_list(request):
    user = User.objects.filter(is_superuser=False, is_staff=False)
    page = "Users list"
    return render(request, 'admin/users/users_list.html', {'user': user, 'page': page})


def UserStatusChange(request, user_id):
    user = User.objects.get(id=user_id)
    if user.is_active == True:
        user.is_active = False
        user.save()
        return redirect('users_list')
    else:
        user.is_active = True
        user.save()
        return redirect('users_list')


def edit_user(request, user_id):
    user = User.objects.get(id=user_id)
    if request.method == "POST":
        user.email = request.POST.get('email')
        user.first_name = request.POST.get('fname')
        user.last_name = request.POST.get('lname')
        user.save()
        return redirect('users_list')
    page = "Edit user"
    return render(request, 'admin/users/edit_user.html', {'page': page, 'user': user})


def user_password_change(request, user_id):
    user = User.objects.get(id=user_id)
    if request.method == "POST":
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')
        if cpassword == password:
            user.set_password(password)
            user.save()
            return redirect('users_list')
        else:
            msg = "Password didn't match. PLease try again!"
            return render(request, 'admin/users/user_password_change.html', {'msg': msg})
    return render(request, 'admin/users/user_password_change.html')


def create_user(request):
    if request.method == "POST":
        first_name = request.POST.get('fname')
        last_name = request.POST.get('lname')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')
        if password == cpassword:
            user = User.objects.create_user(first_name=first_name, last_name=last_name, email=email, username=username)
            user.set_password(password)
            user.is_staff = False
            user.is_superuser = False
            UserType.objects.create(user=user, usertype="User")
            user.save()
            return redirect('users_list')
    page = "Create User"
    return render(request, 'admin/users/create_user.html', {'page': page})


# STREETS

def street_list(request):
    street = Streets.objects.all()
    return render(request, 'admin/streets/street_list.html', {'street': street})


def create_street(request):
    street = Streets.objects.all()
    if request.method == "POST":
        Street_name = request.POST.get("s_name")
        Street_address = request.POST.get('s_address')
        Street_image = request.FILES['s_image']
        st = Streets.objects.create(Street_name=Street_name, Street_address=Street_address, Street_image=Street_image)
        st.Street_status = True
        st.save()
        return redirect('street_list')
    page = "Create Street"
    return render(request, 'admin/streets/create_street.html', {'page': page})


def streetStatusChange(request, id):
    street = Streets.objects.get(id=id)
    if street.Street_status is True:
        street.Street_status = False
        street.save()
        return redirect('street_list')
    else:
        street.Street_status = True
        street.save()
        return redirect('street_list')


def edit_street(request, id):
    street = Streets.objects.get(id=id)
    if request.method == "POST":
        street.Street_name = request.POST.get('s_name')
        street.Street_address = request.POST.get('s_address')
        if 'new_s_image' in request.FILES and request.FILES['new_s_image'].size > 0:
            street.Street_image = request.FILES['new_s_image']
        elif 's_image' in request.POST and request.POST['s_image']:
            street.Street_image = request.POST['s_image']
        street.save()
        return redirect('street_list')
    page = "Edit Street"
    return render(request, 'admin/streets/edit_street.html', {'page': page, 'street': street})


def contact_form(request):
    msg = Contact_Form.objects.all()
    page = "Contact Form List"
    return render(request, 'admin/ContactForm/contactlist.html', {'page': page, 'msg': msg})


### Staffs -------------------------------------------------------------------------------------------------------------------------------------

def staff_users_list(request):
    user = User.objects.filter(is_superuser=False, is_staff=False)
    page = "Users List"
    return render(request, 'staff/users/user_list.html', {'user': user, "page": page})


def staff_UserStatusChange(request, user_id):
    user = User.objects.get(id=user_id)
    if user.is_active == True:
        user.is_active = False
        user.save()
        return redirect('staff_users_list')
    else:
        user.is_active = True
        user.save()
        return redirect('staff_users_list')


def staff_edit_user(request, user_id):
    user = User.objects.get(id=user_id)
    if request.method == "POST":
        user.email = request.POST.get('email')
        user.first_name = request.POST.get('fname')
        user.last_name = request.POST.get('lname')
        user.save()
        return redirect('staff_users_list')
    page = "Edit user"
    return render(request, 'staff/users/edit_users.html', {'page': page, 'user': user})


def staff_create_user(request):
    if request.method == "POST":
        first_name = request.POST.get('fname')
        last_name = request.POST.get('lname')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')
        if cpassword == password:
            if User.objects.filter(username=username).exists():
                msg = "Username already exists. Please try another one!"
                return render(request, 'staff/user/create_user.html', {'msg': msg})
            else:
                user = User.objects.create_user(first_name=first_name, last_name=last_name, email=email,
                                                username=username)
                user.set_password(password)
                user.is_staff = False
                user.is_superuser = False
                user.save()
                return redirect('staff_users_list')

        else:
            msg = "Passwords didn't match. please try again!"
            return render(request, 'staff/users/create_user.html', {'msg': msg})
    page = "Create Staff"
    return render(request, 'staff/users/create_user.html', {'page': page})


def house_requests(request):
    page = "House Request"
    return render(request, 'staff/users/house_request.html', {'page': page})


def profile(request, staff_id):
    staff = User.objects.get(id=staff_id)
    if staff_details.objects.filter(user_id=staff_id).exists():
        details = staff_details.objects.get(user_id=staff_id)
        return render(request, 'staff/staff_profile/profile.html', {'details': details, 'staff': staff})
    else:
        return redirect('create_profile')


def create_profile(request):
    if request.method == "POST":
        user_id = request.POST.get('user_id')
        email = request.POST.get('email')
        staff_land_mark = request.POST.get('staff_land_mark')
        staff_locality = request.POST.get('staff_locality')
        staff_city = request.POST.get('staff_city')
        staff_state = request.POST.get('staff_state')
        staff_country = request.POST.get('staff_country')
        staff_pin = request.POST.get('staff_pin')
        staff_phone = request.POST.get('staff_phone')
        staff_dob = request.POST.get('staff_dob')
        staff_img = request.FILES['staff_img']
        staff_details.objects.create(user_id=user_id,
                                     staff_email=email,
                                     staff_land_mark=staff_land_mark,
                                     staff_locality=staff_locality,
                                     staff_city=staff_city,
                                     staff_state=staff_state,
                                     staff_country=staff_country,
                                     staff_pin=staff_pin,
                                     staff_phone=staff_phone,
                                     staff_dob=staff_dob,
                                     staff_img=staff_img
                                     )
        staff_details.save()
        return redirect('profile', staff_id=user_id)
    page = "Create Staff Profile"
    return render(request, 'staff/staff_profile/create_profile.html', {'page': page})


def edit_staff_profile(request, user_id):
    user = User.objects.get(id=user_id)
    staff = staff_details.objects.get(user_id=user_id)
    if request.method == "POST":
        staff.user_id = request.POST.get('user_id')
        staff.staff_email = request.POST.get('email')
        staff.staff_land_mark = request.POST.get('staff_land_mark')
        staff.staff_locality = request.POST.get('staff_locality')
        staff.staff_city = request.POST.get('staff_city')
        staff.staff_state = request.POST.get('staff_state')
        staff.staff_country = request.POST.get('staff_country')
        staff.staff_pin = request.POST.get('staff_pin')
        staff.staff_phone = request.POST.get('staff_phone')
        staff.staff_dob = request.POST.get('staff_dob')
        if 'new_staff_img' in request.FILES and request.FILES['new_staff_img'].size > 0:
            stf_img = request.FILES['new_staff_img']
        elif 'staff_img' in request.POST and request.POST['staff_img']:
            stf_img = request.POST['staff_img']

        staff.staff_img = stf_img
        staff.save()
        return redirect('profile', staff_id=user_id)
    page = "Edit staff profile"
    return render(request, 'staff/staff_profile/edit_staff_profile.html', {'user': user, 'staff': staff, 'page': page})


##########################

### House owner ------------------------------------------------------------------------------------------------------------------------------
def house_list(request):
    house = House.objects.all()
    page = "House List"
    return render(request, 'HouseOwner/House/house_list.html', {'page': page, 'house': house})


def create_house(request):
    street = Streets.objects.all()
    if request.method == "POST":
        hs_owner = request.user
        hs_number = request.POST.get('hs_number')
        street = request.POST.get('street')
        hs_city = request.POST.get('hs_city')
        hs_state = request.POST.get('hs_state')
        hs_country = request.POST.get('hs_country')
        hs_pin = request.POST.get('hs_pin')
        hs_bhk = request.POST.get('hs_bhk')
        hs_rent = request.POST.get('hs_rent')
        hs_desc = request.POST.get('hs_desc')
        street_instance = Streets.objects.get(Street_name=street)
        house_details = House.objects.create(hs_owner=hs_owner, hs_number=hs_number, street=street_instance,
                                             hs_city=hs_city, hs_state=hs_state, hs_country=hs_country,
                                             hs_pin=hs_pin, hs_bhk=hs_bhk, hs_rent=hs_rent, hs_desc=hs_desc)
        house_details.hs_status = False
        house_details.save()
        return redirect('house_list')
    page = "Create Houses"
    return render(request, 'HouseOwner/House/create_house.html', {'page': page, "street": street})


def houseStatusChange(request, h_id):
    house = House.objects.get(id=h_id)
    if house.hs_status == True:
        house.hs_status = False
        house.save()
        return redirect('house_list')
    elif house.hs_status == False:
        house.hs_status = True
        house.save()
        return redirect('house_list')


def edit_hw(request, h_id):
    hw = House.objects.get(id=h_id)
    street = Streets.objects.all()
    if request.method == "POST":
        hw.hs_owner = request.user
        hw.hs_number = request.POST.get('hs_number')
        street = request.POST.get('street')
        hw.hs_city = request.POST.get('hs_city')
        hw.hs_state = request.POST.get('hs_state')
        hw.hs_country = request.POST.get('hs_country')
        hw.hs_pin = request.POST.get('hs_pin')
        hw.hs_bhk = request.POST.get('hs_bhk')
        hw.hs_rent = request.POST.get('hs_rent')
        hw.hs_desc = request.POST.get('hs_desc')
        street_instance = Streets.objects.get(Street_name = street)
        hw.street = street_instance
        hw.save()
        return redirect('house_list')
    page = "Edit House"
    return render(request, 'HouseOwner/House/edit_house.html', {'page': page, 'hw': hw, 'street': street})
