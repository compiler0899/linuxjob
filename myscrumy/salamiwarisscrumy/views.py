from salamiwarisscrumy.models import ScrumyGoal,GoalStatus,ScrumyHistory
from django.contrib.auth.models import User
from django.db import models
from django.http import HttpResponse
from . import models
from . import form
import random
from django.shortcuts import render
from .form import SignupForm,CreateGoalForm
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import Group
GroupDev=Group.objects.


def index(request):
    if request.method == "POST":
        formGET=form.SignupForm(request.POST)
        if formGET.is_valid():
             newForm = formGET.save(commit = False)
             newForm.set_password(request.POST.get('password'))
             newForm.save()
             GroupDev=Group.objects.get(name='Developer')
             GroupDev.user_set.add(newForm)
             

        return HttpResponse('YOUR NEW PROFILE HAS BEEN CREATED')
        
    else:
        formGET =form.SignupForm() 
        context={
            "form":formGET
        }
        return render(request,"salamiwarisscrumy/index.html",context)          


def move_goal(request,goal_id):
    if request.method == 'POST':
        Agoal=models.ScrumyGoal.objects.get(goal_id = goal_id)
        weeklygoal=models.GoalStatus.objects.get(status_name = "Weekly_Goal")
        dailygoal=models.GoalStatus.objects.get(status_name="Daily Goal")
        verify = models.GoalStatus.objects.get(status_name="Verify Goal")
        done =models.GoalStatus.objects.get(status_name="Done Goal")
        ActiveUser = request.user
        Group

def add_goal(request):
    
    if request.method == 'POST':
        FormAdd = form.CreateGoalForm(request.POST)
        if FormAdd.is_valid():
            NewGoal=FormAdd.save(commit=False)
            get_scrumy_objects=ScrumyGoal.objects.all() # this line of code  will  get all objects in ScrumyGoals
            def id_checker():#this function is used to choose a random id and check if the id has not existing before
                checker=[x.goal_id for x in get_scrumy_objects] #this is to create a list of already existing id
                number= random.randint(1000,10000)
                if number in checker:
                    return id_checker()
                else:
                    iid = number
                    return iid
            id_get=id_checker()
            NewGoal.goal_id=id_get

            goalstatus=GoalStatus.objects.all() # this line of code  will  get all objects in GoalStatus
            goal_stat=[e.status_name for e in goalstatus] #this is to create a list of all status 
            goalget=GoalStatus.objects.get(status_name=random.choice(goal_stat)) # this choose random goal_status for each user when creating goal
            NewGoal.goal_status=goalget                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
            NewGoal.save()
        return HttpResponse('YOUR NEW GOAL HAS BEEN CREATED SUCCESSFULLY')
    else:
        FormAdd = form.CreateGoalForm()
        context = {
            'form':FormAdd
        }

        return render(request,'salamiwarisscrumy/addgoal.html',context)


def home(request):
    users=User.objects.all()
    W=GoalStatus.objects.get(status_name="Weekly_Goal")
    Da=GoalStatus.objects.get(status_name="Daily Goal")
    Vf=GoalStatus.objects.get(status_name="Verify Goal")
    Do=GoalStatus.objects.get(status_name="Done Goal")
    weeklygoal=ScrumyGoal.objects.filter(goal_status=W)
    daily=ScrumyGoal.objects.filter(goal_status=Da)
    verify=ScrumyGoal.objects.filter(goal_status=Vf)
    done=ScrumyGoal.objects.filter(goal_status=Do)
    dico = {"weeklygoal":weeklygoal,"Users":users,"daily":daily,"verify":verify,"done":done}
    return render(request,'salamiwarisscrumy/home.html',dico)