from django.urls import path
from .views import *

urlpatterns = [
    # user actions     
    path('new_user/' , Account_view.new_user , name= "new_user" ),
    path('login/' , Account_view.login_view , name= "login" ),
    path('verify/<str:auth_token>/' , Account_view.verify_mail , name= "verify_mail"),
    path('logout/' , Account_view.logout_view , name= "logout" ),
    path('change_password/' , Account_view.change_password , name= "change_password" ),
    path('forgot_password/' , Account_view.forgot_password , name= "forgot_password" ),
    path('delete_user/' , Account_view.delete_user , name= "delete_user" ),
    
    # profile actions

    path('profile_edit/' , Profile_view.edit_profile_view , name= 'edit_profile' ),
    
    #profile actions
    path('profile/' , Profile_view.profile , name= 'profile' ),
    
    # user account settings 
    path('settings/' , Profile_view.settings_view, name= 'settings' ),
    #change email
    path('change_email/' , Profile_view.change_email , name= 'change_email' ),
    # change password
    path('change_password/' , Account_view.change_password , name= 'change_password' ),
    
    #admin actions

    path('manage_user/' , AdminAction.manage_accounts , name= 'manage_user' ),
    path('view_profile/<int:id>' , AdminAction.view_profile , name= 'view_profile' ),
    path('delete_user_by_admin/<int:id>/' , AdminAction.delete_user_by_admin , name= 'delete_user_by_admin' ),
    
    
    
]
