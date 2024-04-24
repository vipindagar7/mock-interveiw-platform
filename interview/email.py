from django.conf import settings
from django.core.mail import send_mail
from django.contrib import messages

def send_mail_for_schedule_session_to_user(request, interviewer_email, user_email, domain, date, time):
    subject = 'Interview Scheduled'
    message = f'Hello,\n\nYou have requested a mock interview session with {interviewer_email} for {domain} on {date} at {time}.\n\nYou will be notified once the interviewer accepts the request.\n\nThank you.\n\nTeam Interview.'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [user_email]
    send_mail(subject, message, email_from, recipient_list)
    messages.success(request, f"Session scheduled with {interviewer_email}")
    return None

def send_mail_for_schedule_session_to_interviewer(request, interviewer_email, user_email, domain, date, time):
    subject = 'Interview Request'
    message = f'Hello,\n\n{user_email} has requested a mock interview session with you for {domain} on {date} at {time}.\n\nPlease update the status on the website.\n\nThank you.\n\nTeam Interview.'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [interviewer_email]
    send_mail(subject, message, email_from, recipient_list)
    return None

def send_mail_for_update_session_status(request, interviewer_email, user_email, domain, date, time, status):
    subject = 'Interview Status Update'
    message = f'Hello,\n\nYour interview with {interviewer_email} for {domain} on {date} at {time} has been {status}.\n\nYou can check the updated status on the website.\n\nThank you.\n\nTeam Interview.'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [user_email]
    send_mail(subject, message, email_from, recipient_list)
    return None
