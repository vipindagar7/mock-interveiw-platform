# signals.py

from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Custom_user, InterviewerProfile, UserProfile

@receiver(post_save, sender=Custom_user)
def create_profile(sender, instance, created, **kwargs):
    if created:
        if instance.is_interviewer:
            InterviewerProfile.objects.create(user=instance)
        else:
            UserProfile.objects.create(user=instance)

@receiver(post_save, sender=Custom_user)
def save_profile(sender, instance, **kwargs):
    if instance.is_interviewer:
        instance.interviewerprofile.save()
    else:
        instance.userprofile.save()
