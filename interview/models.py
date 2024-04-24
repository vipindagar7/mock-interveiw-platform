from django.db import models

from account.models import Custom_user


# # Create your models here.
class Session(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Custom_user, on_delete=models.CASCADE)
    domain = models.CharField(max_length=255)
    question1 = models.TextField()
    demo_answer1 = models.TextField()
    question2 = models.TextField()
    demo_answer2 = models.TextField()
    question3 = models.TextField()
    demo_answer3 = models.TextField()
    question4 = models.TextField()
    demo_answer4 = models.TextField()
    question5 = models.TextField()
    demo_answer5 = models.TextField()
    question6 = models.TextField()
    demo_answer6 = models.TextField()
    question7 = models.TextField()
    demo_answer7 = models.TextField()
    question8 = models.TextField()
    demo_answer8 = models.TextField()
    question9 = models.TextField()
    demo_answer9 = models.TextField()
    question10 = models.TextField()
    demo_answer10 = models.TextField()
    
    
class AnsweredSession(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Custom_user, on_delete=models.CASCADE)
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    domain = models.CharField(max_length=255)
    question1 = models.TextField()
    user_answer1 = models.TextField(null = True, blank = True)
    question2 = models.TextField()
    user_answer2 = models.TextField(null = True, blank = True)
    question3 = models.TextField()
    user_answer3 = models.TextField(null = True, blank = True)
    question4 = models.TextField()
    user_answer4 = models.TextField(null = True, blank = True)
    question5 = models.TextField()
    user_answer5 = models.TextField(null = True, blank = True)
    question6 = models.TextField()
    user_answer6 = models.TextField(null = True, blank = True)
    question7 = models.TextField()
    user_answer7 = models.TextField(null = True, blank = True)
    question8 = models.TextField()
    user_answer8 = models.TextField(null = True, blank = True)
    question9 = models.TextField()
    user_answer9 = models.TextField(null = True, blank = True)
    question10 = models.TextField()
    user_answer10 = models.TextField(null = True, blank = True)
    
    
    
    
class ScheduleInterview(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Custom_user, on_delete=models.CASCADE)
    interviewer = models.ForeignKey(Custom_user, on_delete=models.CASCADE , related_name = 'interviewer')
    domain = models.CharField(max_length=255)
    date = models.DateField()
    time = models.TimeField()
    status = models.CharField(max_length=255 , default = 'confirmation pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
