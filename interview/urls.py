from django.urls import path
from .views import home , select_domain , interview_session , schedule_session


urlpatterns = [
    path("", home, name="home-interview"),
    path("select-domain/", select_domain, name="select-domain"),
    path("session/", interview_session.session , name="interview-session"),
    path("feedback/", interview_session.feedback , name="interview-feedback"), 
    path("session_history/", interview_session.session_history , name="session_history"), 
    path("view_session/<int:id>/", interview_session.view_session , name="view_session"), 
    path("delete_session/<int:id>/", interview_session.delete_session , name="delete_session"), 



    path("view_interviewers/", schedule_session.view_interviewers , name="view_interviewers"), 
    path("schedule_interview/<int:id>/", schedule_session.schedule_interview , name="schdule_interview"),

    path("schduled_session/", schedule_session.scheduled_interview , name="schdule_interview"),
    
    path("view_schedule/<int:id>/", schedule_session.view_schedule , name="view_schdeule"),
    path("delete_schedule/<int:id>/", schedule_session.delete_schedule , name="view_schdeule"),
     
    
    
    
    
]



