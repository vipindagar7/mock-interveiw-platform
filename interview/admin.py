from django.contrib import admin
from .models import Session , AnsweredSession , ScheduleInterview
# Register your models here.
admin.site.register(Session)
admin.site.register(AnsweredSession)
admin.site.register(ScheduleInterview)