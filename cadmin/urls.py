from django.urls import path
from . import views

urlpatterns = [

    # Login
    path('' , views.admin_login , name="admin_login"),
    path('staff_login' , views.staff_login , name="staff_login"),

    # Logout    
    path('admin_logout' , views.admin_logout , name="admin_logout"),


    # Dashboard
    path('dashboard' , views.dashboard , name="dashboard"),
    path('staff_dashboard' , views.staff_dashboard , name="staff_dashboard"),
    path('read_msg/<int:msg_id>' , views.read_msg , name="read_msg"),
    path('hw_dashboard' , views.hw_dashboard , name="hw_dashboard"),

    ### Admin ------------------------------------------------------------------------------------------------------------------------------------

    # Staff
    path('create_staff' , views.create_staff , name="create_staff"),
    path('staff_list' , views.staff_list , name="staff_list"),
    path('StaffStatusChange/<int:user_id>' , views.StaffStatusChange , name="StaffStatusChange"),
    path('edit_staff/<int:staff_id>' , views.edit_staff , name="edit_staff"),
    path('staff_passwordchange/<int:staff_id>' , views.staff_passwordchange , name="staff_passwordchange"),

    # Users 
    path('users_list' , views.users_list , name="users_list"),
    path('UserStatusChange/<int:user_id>' , views.UserStatusChange , name="UserStatusChange"),
    path('edit_user/<int:user_id>' , views.edit_user , name="edit_user"),
    path('user_password_change/<int:user_id>' , views.user_password_change , name="user_password_change"),
    path('create_user' , views.create_user , name="create_user"),

    # House owner
    path('hwlist' , views.hwlist , name="hwlist"),
    path('createhw' , views.createhw , name="createhw"),
    path('edit_hw/<int:h_id>' , views.edit_hw , name="edit_hw"),

    # Streets
    path('create_street' , views.create_street , name="create_street"),
    path('street_list' , views.street_list , name="street_list"),
    path('streetStatusChange/<int:id>', views.streetStatusChange, name="streetStatusChange"),
    path('edit_street/<int:id>', views.edit_street, name="edit_street"),

    # Contact Form
    path('contact_form', views.contact_form, name="contact_form" ),


    #Page links

    ### Staffs ------------------------------------------------------------------------------------------------------------------------------------
       
        #Users
        path('staff_users_list' , views.staff_users_list , name="staff_users_list"),
        path('staff_UserStatusChange/<int:user_id>' , views.staff_UserStatusChange , name="staff_UserStatusChange"),
        path('staff_edit_user/<int:user_id>' , views.staff_edit_user , name="staff_edit_user"),
        path('staff_create_user' , views.staff_create_user , name="staff_create_user"),

        # Staff profile
        path('create_profile/<int:staff_id>' , views.create_profile , name="create_profile"),
        path('edit_staff_profile/<int:user_id>' , views.edit_staff_profile , name="edit_staff_profile"),

        #Page links
        path('house_requests' , views.house_requests , name="house_requests"),
        path('profile/<int:staff_id>' , views.profile , name="profile"),

        # House Request
        path('req_accept/<int:id>' , views.req_accept , name="req_accept"),
        path('req_reject/<int:id>' , views.req_reject , name="req_reject"),

    ### House owner -------------------------------------------------------------------------------------------------------------------------------

        # House owner
        path('hwStatusChange/<int:id>', views.hwStatusChange , name="hwStatusChange"),
        path('hw_house_request/', views.hw_house_request, name="hw_house_request"),
        path('hw_req_accept/<int:id>' , views.hw_request_accept , name="hw_request_accept"),


        #House 
        path('house_list/<int:user_id>' , views.house_list , name = "house_list"),
        path('create_house' , views.create_house , name="create_house"),
        path('houseStatusChange/<int:h_id>' , views.houseStatusChange , name="houseStatusChange"),
        path('delete_req/<int:id>' , views.delete_req, name="delete_req")



]