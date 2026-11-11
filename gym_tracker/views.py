from django.shortcuts import render
from .models import Member,WorkoutLog
# Create your views here.

def member_list(view_request):
    members = Member.objects.all()#get by ORM
    context = {'members':members}
    return render(view_request,'gym_tracker/member_list.html',context)
