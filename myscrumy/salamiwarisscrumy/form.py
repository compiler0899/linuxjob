from django.db import models
from django.forms import ModelForm,PasswordInput
from salamiwarisscrumy.models import ScrumyGoal,GoalStatus,ScrumyHistory
from django.contrib.auth.models import User

from django.forms import models
class SignupForm(ModelForm):
    class Meta:
        model=User
        fields = ["first_name","last_name","email","username","password"]
        widgets={
            "password":PasswordInput(),
        }
    

class CreateGoalForm(ModelForm):
    class Meta:
        model=ScrumyGoal
        fields =["goal_name","user"]