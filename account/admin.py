from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Custom_user)
admin.site.register(UserProfile)
admin.site.register(InterviewerProfile)