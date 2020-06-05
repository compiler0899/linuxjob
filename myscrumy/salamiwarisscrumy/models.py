from django.db import models
from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class GoalStatus(models.Model):
    status_name = models.CharField(max_length=200)
    def __str__(self):
        return self.status_name





class ScrumyGoal(models.Model):
    def __str__(self):
        return self.goal_name
	
    goal_name = models.CharField(max_length=255)
    goal_id = models.IntegerField(default = 18)
    created_by = models.CharField(max_length=255)
    moved_by = models.CharField(max_length=200)
    owner = models.CharField(max_length=200)
    goal_status = models.ForeignKey(GoalStatus,on_delete = models.PROTECT)
    user = models.ForeignKey(User,on_delete=models.PROTECT,related_name='gow')




class ScrumyHistory(models.Model):
    def __str__(self):
        return self.created_by
    moved_by = models.CharField(max_length=200)
    created_by = models.CharField(max_length=200)
    moved_from = models.CharField(max_length=200)
    moved_to =models.CharField(max_length=200)
    time_of_action = models.DateTimeField(default=timezone.now)
    goal = models.ForeignKey(ScrumyGoal,on_delete=models.PROTECT)
    

