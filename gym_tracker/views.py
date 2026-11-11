from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from .forms import MemberForm, WorkoutLogForm
from .models import Member, WorkoutLog


def member_list(request):
    members = Member.objects.all().order_by('first_name', 'last_name')
    return render(request, 'gym_tracker/member_list.html', {'members': members})


def member_add(request):
    form = MemberForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'המתאמן נוסף בהצלחה')
        return redirect('member_list')
    return render(request, 'gym_tracker/form.html', {'form': form, 'title': 'הוספת מתאמן', 'back_url': 'member_list'})


@require_POST
def member_delete(request, pk):
    member = get_object_or_404(Member, pk=pk)
    member.delete()  # associated WorkoutLog records are deleted via CASCADE
    messages.success(request, 'המתאמן נמחק בהצלחה')
    return redirect('member_list')


def workout_list(request):
    workouts = WorkoutLog.objects.select_related('member').order_by('-id')
    return render(request, 'gym_tracker/workout_list.html', {'workouts': workouts})


def workout_add(request):
    form = WorkoutLogForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'האימון נוסף בהצלחה')
        return redirect('workout_list')
    return render(request, 'gym_tracker/form.html', {'form': form, 'title': 'הוספת אימון', 'back_url': 'workout_list'})


@require_POST
def workout_delete(request, pk):
    workout = get_object_or_404(WorkoutLog, pk=pk)
    workout.delete()
    messages.success(request, 'האימון נמחק בהצלחה')
    return redirect('workout_list')
