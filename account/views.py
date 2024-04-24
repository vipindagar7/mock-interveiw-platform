from django.shortcuts import render , HttpResponse ,redirect
import os
from django.contrib.auth import authenticate ,login ,logout
from django.contrib.auth.decorators import login_required
from .models import Custom_user , UserProfile , InterviewerProfile
import uuid
from .forms import LoginForm , NewUserForm
from django.conf import settings
from django.core.mail import send_mail
from django.contrib import messages
from .email import *
from interview.models import Session , AnsweredSession


User = Custom_user


class Account_view:
    
    def new_user(request):
        if request.method == "POST":
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            email = request.POST.get('email')
            email = email.lower()
            password = request.POST.get('password')
            is_interviewer = request.POST.get('is_interviewer')
            if is_interviewer == "on":
                is_interviewer = True
            else:
                is_interviewer = False
            try:
                if Custom_user.objects.filter(email=email).first():
                    messages.error(request,  email + " is already taken")
                    return redirect('/accounts/new_user/')
                auth_token =  str(uuid.uuid4())
                user_obj = Custom_user.objects.create_user(email=email , first_name=first_name, last_name=last_name , auth_token =auth_token, is_interviewer=is_interviewer)
                user_obj.set_password(password)
                user_obj.save()
                
                send_verification_email(email , auth_token)
                if send_verification_email:                
                    messages.success(request, "check" + email + " for verification link")
                    return redirect('/accounts/login/')
                else:
                    return HttpResponse("error in sending email")
    
            except Exception as e:
                return HttpResponse(e)
        context = {'form': NewUserForm()}
        return render(request, "account/new_user.html" , context)
    
    def verify_mail(request , auth_token):
        try:
            user = User.objects.filter(auth_token=auth_token).first()
            if user:
                if user.is_verified:
                    messages.success(request, "user is already verified")
                    return redirect("/accounts/login/")
                user.is_verified = True
                user.save()
                messages.success(request, "user has been verified")
                return redirect("/account/login/")
            else:
                messages.error(request, "user not found")
                return redirect("/accounts/login/")
        except Exception as e:
            return HttpResponse(e)
    
    def login_view(request):
        if request.method == "POST":
            form = LoginForm(request.POST)
            if form.is_valid():
                email = form.cleaned_data['email']
                
                password = form.cleaned_data['password']
                user = authenticate(request , email = email.lower() , password = password)
    
                if user is not None:
                    if user.is_verified:
                        login(request, user)
                        return redirect(f"/accounts/profile/")
                    else:
                        messages.error(request, "Email is not verified")
                        return redirect('/accounts/login/')
                messages.error(request, "Invalid credentials")
                return redirect('/accounts/login/')
        context = {'loginForm': LoginForm()}
        return render(request, "account/login.html" , context)
    
    def logout_view(request):
        logout(request)
        return redirect('/accounts/login/')
    
    def change_password(request):
      if request.method == "POST":
          new_password = request.POST.get('new_password')
          new_password_confirmation = request.POST.get('new_password_confirmation')
          if new_password == new_password_confirmation:
              user = Custom_user.objects.get(email= request.user)                
              user.set_password(new_password_confirmation)
              user.save()
              messages.success(request, "Password changed")
              return redirect('/accounts/settings/')
          else:
              messages.error(request, "Password not matched")
              return redirect('/accounts/settings/')
    
    def forgot_password(request):
        try:
            if request.method == "POST":
                email = request.POST.get('email')
                user = User.objects.filter(email=email).first()
                if user:
                    auth_token = str(uuid.uuid4())
                    user.auth_token = auth_token
                    user.save()
                    send_password_reset_email(email , auth_token)
                    if send_password_reset_email:
                        messages.success(request, "Password reset link sent to your email")
                        return redirect('account/login/')
                    else:
                        
                        messages.success(request, "error in Password reset link sending to your email")
                        return redirect('account/forgot-password/')
                else:
                    messages.error(request, 'user not found')
                    return redirect('/account/forgot-password/')
            return render(request, "account/forgot-password.html")
        except Exception as e:
            return HttpResponse(e)
    @login_required
    def delete_user(request):
        if request.method == "POST":
            password = request.POST.get('password')
            user = authenticate(request , email = request.user.email , password = password)
            if user is not None:
                user = Custom_user.objects.get(email= request.user.email)                
                user.delete()
                send_delete_account_mail(request.user.email)
                messages.success(request, "user deleted")
                return redirect('/accounts/login/')
            else:
                messages.error(request, "Invalid credentials")
                return redirect('/accounts/settings/')
        return HttpResponse("404 page not found")
    
class Profile_view:
    @login_required
    def profile(request):
        user = Custom_user.objects.get(email= request.user.email)        
        if user.is_interviewer:
            profile = InterviewerProfile.objects.get(user=user)
        else:
            profile = UserProfile.objects.get(user=user)
        context = {'user': user , 'profile': profile}
        return render(request, "account/profile.html",context) 
        
    @login_required
    def edit_profile_view(request):
        user = Custom_user.objects.get(email= request.user.email)        
        if user.is_interviewer:
            profile = InterviewerProfile.objects.get(user=user)
        else:
            profile = UserProfile.objects.get(user=user)
        context = {'user': user , 'profile': profile}
        if request.method == "POST" :
            user.first_name = request.POST.get('first_name')
            user.last_name = request.POST.get('last_name')
            user.email = request.POST.get('email').lower()
            user.save()
            profile.field = request.POST.get('field')
            profile.mobile = request.POST.get('mobile')
            profile.location = request.POST.get('location')
            profile.twitter = request.POST.get('twitter')
            profile.github = request.POST.get('github')
            profile.linkedin = request.POST.get('linkedin')
            profile.instagram = request.POST.get('instagram')
            profile.bio = request.POST.get('bio')
            profile.skills = request.POST.get('skills')
            profile.intrests = request.POST.get('intrests')

            profile.company = request.POST.get('company')
            profile.position = request.POST.get('position')
            profile.experience = request.POST.get('experience')
            if request.FILES:
                profile.image = request.FILES["profile"]
            
            
            
            
            profile.save()
            print(profile)
            return redirect('/accounts/profile/')
        return render(request, "account/edit_profile.html",context)
    
    
    @login_required
    def settings_view(request):
        user = Custom_user.objects.get(email= request.user.email)
        if user.is_interviewer:
            profile = InterviewerProfile.objects.get(user=user)
        else:        
            profile = UserProfile.objects.get(user=user)
        context = {'user': user , 'profile': profile}
        return render(request, "account/settings.html",context)
    
    @login_required
    def change_email(request):
        if request.method == "POST":
            new_email = request.POST.get('new_email')
            send_verification_email(new_email, request.user.auth_token)
            user = Custom_user.objects.get(email= request.user.email)                
            user.is_verified = False
            user.email = new_email
            user.save()
            messages.success(request, "check your email for verification link")
            return redirect('/accounts/settings/')
        return HttpResponse("404 page not found")
    
    
    
class AdminAction:
    @login_required
    def manage_accounts(request):
        user = Custom_user.objects.get(email= request.user.email)
        if user.is_superuser:
            accounts = Custom_user.objects.all()
            context = {'accounts': accounts}
            return render(request, 'account/admin/manage_account.html', context)
        return HttpResponse("404 page not found")

        
    @login_required
    def view_profile(request , id):
        login_user = Custom_user.objects.get(email= request.user.email)
        if login_user.is_superuser:
            user = Custom_user.objects.get(id= id)
            if request.method == "POST":
                user.email = request.POST.get('email')
                user.save()
                messages.success(request, "email changed")
                return redirect('/accounts/manage_user/')
            if user.is_interviewer:
                profile = InterviewerProfile.objects.get(user=user)
            else:   
                profile = UserProfile.objects.get(user=user)
            context = {'profile': profile}
            return render(request, "account/admin/view_profile.html",context)
        return HttpResponse("404 page not found")
    
    
    def delete_user_by_admin(request, id):
        admin = Custom_user.objects.get(email= request.user.email)
        if admin.is_superuser:
            user = Custom_user.objects.get(id= id)
            user.delete()
            messages.success(request,"User deleted succefully")
            return redirect('/accounts/manage_user/')
        else:
            return HttpResponse("404 page not found")


