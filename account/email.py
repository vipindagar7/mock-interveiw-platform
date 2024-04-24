from django.conf import settings
from django.core.mail import send_mail

domain = 'vipindagar.works'

def send_verification_email(email, token):
    subject = "Your Account Verification"
    message = f"Dear User,\n\nClick on the link below to verify your account:\n\ http://127.0.0.1:8000/accounts/verify/{token}\n\nThank you,\nTeam Global Interview Simulate"
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, email_from, recipient_list)
    
def send_password_reset_email(email, token):
    subject = "Password Reset Request"
    message = f"Dear User,\n\nClick on the link below to reset your password:\n\nhttp://localhost.com/reset-password/{token}\n\nThank you,\nTeam Global Interview Simulate"
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, email_from, recipient_list)
    
def send_verification_new_email(email, token):
    subject = "Your Account Verification"
    message = f"Dear User,\n\nClick on the link below to verify your new email address:\n\nhttp://127.0.0.1:8000/accounts/verify/{token}\n\nThank you,\nTeam Global Interview Simulate"
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, email_from, recipient_list)
    
def send_delete_account_mail(email):
    subject = "Account Deletion Confirmation"
    message = f"Dear User,\n\nYour account has been successfully deleted.\n\nThank you for using our service.\n\nTeam Global Interview Simulate"
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, email_from, recipient_list)
