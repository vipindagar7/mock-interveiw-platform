from django.shortcuts import render , HttpResponse , redirect
from django.http import JsonResponse
from .questions import question_generator
from .models import Session , AnsweredSession
from django.contrib.auth.decorators import login_required
from account.models import Custom_user , InterviewerProfile , UserProfile
from .models import ScheduleInterview
from django.contrib import messages
from .email import * 
from .feedback import generate_feedback
# Create your views here.
@login_required
def home(request):
    return render(request , 'interview/interview.html')

@login_required
def select_domain(request):
    user = Custom_user.objects.get(email = request.user.email)
    if user.is_interviewer and user.is_superuser:
        return HttpResponse('404 not found')
    else:
        return render(request , 'interview/select-domain.html')


class interview_session:
   
    @login_required
    def session(request):
        user = request.user
        if user.is_interviewer and user.is_superuser:
            return HttpResponse('404 not found')
        else:
            if request.method == 'POST':
                domain = request.POST.get('domain')
                questions = question_generator(domain)
                question1= questions[0]['question']
                demo_answer1= questions[0]['answer']
                question2= questions[1]['question'] 
                demo_answer2= questions[1]['answer']
                question3= questions[2]['question']
                demo_answer3= questions[2]['answer']
                question4= questions[3]['question']
                demo_answer4= questions[3]['answer']
                question5= questions[4]['question']
                demo_answer5= questions[4]['answer']
                question6= questions[5]['question']
                demo_answer6= questions[5]['answer']
                question7= questions[6]['question']
                demo_answer7= questions[6]['answer']
                question8= questions[7]['question']
                demo_answer8= questions[7]['answer']
                question9= questions[8]['question']
                demo_answer9= questions[8]['answer']
                question10= questions[9]['question']
                demo_answer10= questions[9]['answer']
                session = Session.objects.create(
                    user = request.user,
                    domain = domain,
                    question1 = question1,
                    demo_answer1 = demo_answer1,
                    question2 = question2,
                    demo_answer2 = demo_answer2,
                    question3 = question3,
                    demo_answer3 = demo_answer3,
                    question4 = question4,
                    demo_answer4 = demo_answer4,
                    question5 = question5,
                    demo_answer5 = demo_answer5,
                    question6 = question6,
                    demo_answer6 = demo_answer6,
                    question7 = question7,
                    demo_answer7 = demo_answer7,
                    question8 = question8,
                    demo_answer8 = demo_answer8,
                    question9 = question9,
                    demo_answer9 = demo_answer9,
                    question10 = question10,
                    demo_answer10 = demo_answer10
                )
                session.save()
                context = {'questions': questions , 'domain': domain , 'session': session}
                
                return render(request, 'interview/interview-session.html', context)

            return render(request, 'interview/interview-session.html')
        

    
    @login_required
    def feedback(request):
        if request.method == 'POST':         
            domain = request.POST.get('domain')
            session = request.POST.get('session')   
            question0 = request.POST.get('question0')
            answer0 = request.POST.get('answer_input0')
            question1 = request.POST.get('question1')
            answer1 = request.POST.get('answer_input1')
            question2 = request.POST.get('question2')
            answer2 = request.POST.get('answer_input2')
            question3 = request.POST.get('question3')
            answer3 = request.POST.get('answer_input3')
            question4 = request.POST.get('question4')
            answer4 = request.POST.get('answer_input4')
            question5 = request.POST.get('question5')
            answer5 = request.POST.get('answer_input5')
            question6 = request.POST.get('question6')
            answer6 = request.POST.get('answer_input6')
            question7 = request.POST.get('question7')
            answer7 = request.POST.get('answer_input7')
            question8 = request.POST.get('question8')
            answer8 = request.POST.get('answer_input8')
            question9 = request.POST.get('question9')
            answer9 = request.POST.get('answer_input9')
            answered_session = AnsweredSession.objects.create(
                user = request.user,
                domain = request.POST.get('domain'),
                session = Session.objects.get(id = session),
                question1 = question0,
                user_answer1 = answer0,
                question2 = question1,
                user_answer2 = answer1,
                question3 = question2,
                user_answer3 = answer2,
                question4 = question3,
                user_answer4 = answer3,
                question5 = question4,
                user_answer5 = answer4,
                question6 = question5,
                user_answer6 = answer5,
                question7 = question6,
                user_answer7 = answer6,
                question8 = question7,
                user_answer8 = answer7,
                question9 = question8,
                user_answer9 = answer8,
                question10 = question9,
                user_answer10 = answer9
            )
            answered_session.save()
            feedback = generate_feedback(domain ,question0, answer0, question1, answer1, question2, answer2, question3, answer3, question4, answer4, question5, answer5, question6, answer6, question7, answer7, question8, answer8, question9, answer9)
            demo_answers =  Session.objects.filter(id = session)
            context = {'question0': question0, 'answer0': answer0, 'demo_answer1': demo_answers[0].demo_answer1,
                       'question1': question1, 'answer1': answer1, 'demo_answer2': demo_answers[0].demo_answer2,
                         'question2': question2, 'answer2': answer2, 'demo_answer3': demo_answers[0].demo_answer3,
                         'question3': question3, 'answer3': answer3, 'demo_answer4': demo_answers[0].demo_answer4,
                         'question4': question4, 'answer4': answer4, 'demo_answer5': demo_answers[0].demo_answer5,
                         'question5': question5, 'answer5': answer5, 'demo_answer6': demo_answers[0].demo_answer6,
                         'question6': question6, 'answer6': answer6, 'demo_answer7': demo_answers[0].demo_answer7,
                         'question7': question7, 'answer7': answer7, 'demo_answer8': demo_answers[0].demo_answer8,
                         'question8': question8, 'answer8': answer8, 'demo_answer9': demo_answers[0].demo_answer9,
                         'question9': question9, 'answer9': answer9,'demo_answer10': demo_answers[0].demo_answer10,
                        #  'demo_answers' : demo_answers,
                         'domain':domain,
                        'session': session,
                        'feedback': feedback,
                        
                         }
            return render(request, 'interview/interview-feedback.html', context)
        return HttpResponse('404 not found')
   
    @login_required
    def session_history(request):
        created_session = Session.objects.filter(user=request.user).all()
        answered_session = AnsweredSession.objects.filter(user = request.user).all()
        context = {'created_session': created_session , 'answered_session': answered_session}
        return render(request, 'interview/session_history.html', context)
        
    @login_required
    def view_session(request,id):
        if request.method == "POST":
            id = request.POST.get('id')
            domain = request.POST.get('domain')
            question0 = request.POST.get('question0')
            answer0 = request.POST.get('user_answer0')
            question1 = request.POST.get('question1')
            answer1 = request.POST.get('user_answer1')
            question2 = request.POST.get('question2')
            answer2 = request.POST.get('user_answer2')
            question3 = request.POST.get('question3')
            answer3 = request.POST.get('user_answer3')
            question4 = request.POST.get('question4')
            answer4 = request.POST.get('user_answer4')
            question5 = request.POST.get('question5')
            answer5 = request.POST.get('user_answer5')
            question6 = request.POST.get('question6')
            answer6 = request.POST.get('user_answer6')
            question7 = request.POST.get('question7')
            answer7 = request.POST.get('user_answer7')
            question8 = request.POST.get('question8')
            answer8 = request.POST.get('user_answer8')
            question9 = request.POST.get('question9')
            answer9 = request.POST.get('user_answer9')
            feedback = generate_feedback(domain ,question0, answer0, question1, answer1, question2, answer2, question3, answer3, question4, answer4, question5, answer5, question6, answer6, question7, answer7, question8, answer8, question9, answer9)
            session = AnsweredSession.objects.get(session=id)
            context = {'session': session , 'feedback':feedback}
            return render(request, 'interview/view_session.html', context)
            
        session = AnsweredSession.objects.get(session=id)
        context = {'session': session}
        return render(request, 'interview/view_session.html', context)

    def delete_session(request , id):
        session = Session.objects.get(id=id)
        session.delete()
        return redirect('/interview/session_history/')
    
class schedule_session:
    @login_required
    def view_interviewers(request):
        if not request.user.is_interviewer and not request.user.is_superuser:
            interviewer = InterviewerProfile.objects.all()
            context = {'interviewer' : interviewer}
            return render(request, 'interview/view_interviewer.html' , context)
        return HttpResponse('404 not found')
    
    @login_required
    def schedule_interview(request , id):
        if not request.user.is_interviewer and not request.user.is_superuser:
            if request.method == 'POST':
                domain = request.POST.get('domain')
                date = request.POST.get('date')
                time = request.POST.get('time')
                user = request.user
                interviewer = InterviewerProfile.objects.get(id = id).user
                schedule = ScheduleInterview.objects.create(
                    user = user,
                    interviewer = interviewer,
                    domain = domain,
                    date = date,
                    time = time
                )
                schedule.save()
                send_mail_for_schedule_session_to_user(request, interviewer.email, user.email, domain, date, time)
                send_mail_for_schedule_session_to_interviewer(request, interviewer.email, user.email, domain, date, time)
                messages.success(request, f"session scheduled with {interviewer}")
                return redirect('/interview/schduled_session/')
            interviewer = InterviewerProfile.objects.get(id = id)
            context = {'interviewer' : interviewer}
            return render(request, 'interview/schedule_interview.html' , context)
        return HttpResponse('404 not found')
    
    
    
    @login_required
    def scheduled_interview(request):
        if not request.user.is_superuser:
            if request.user.is_interviewer:
                scheduled_session = ScheduleInterview.objects.filter(interviewer=request.user).all()
                if request.method == 'POST':
                    id = request.POST.get('id')
                    session = ScheduleInterview.objects.get(id=id)
                    session.status = request.POST.get('status')
                    session.save()
                    send_mail_for_update_session_status(request, session.interviewer.email, session.user.email, session.domain, session.date, session.time, session.status)
                    return redirect('/interview/schduled_session/')
            else:    
                scheduled_session = ScheduleInterview.objects.filter(user=request.user).all()
                
            context = {'scheduled_session': scheduled_session}
            return render(request, 'interview/scheduled_session.html', context)
        
        return HttpResponse('404 not found')
    
    
    @login_required
    def view_schedule(request, id):
        user = request.user
        if user.is_interviewer:
            session = ScheduleInterview.objects.get(interviewer=request.user , id=id)
        else:
            session = ScheduleInterview.objects.get(user=request.user , id=id)
        context = {'session': session}
        return render(request, 'interview/view_scheduled.html', context)
    
    @login_required
    def delete_schedule(request , id):
        session = ScheduleInterview.objects.get(id=id)
        if session.user == request.user:
            session.delete()
            messages.success(request, f"session deleted successfully")
        else:
            messages.warning(request, f"you are not authorized to delete this session")
        return redirect('/interview/schduled_session/')
            