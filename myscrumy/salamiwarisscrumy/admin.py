from django.contrib import admin
from .models import ScrumyGoal,GoalStatus,ScrumyHistory

admin.site.register(ScrumyGoal)
admin.site.register(ScrumyHistory)
admin.site.register(GoalStatus)
