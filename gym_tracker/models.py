from django.db import models


# Create your models here.
class Member(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    joined_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class WorkoutLog(models.Model):

    member = models.ForeignKey(Member, on_delete=models.CASCADE,related_name='workouts')
    exercise_name = models.CharField(max_length=100)
    sets = models.IntegerField()
    reps = models.IntegerField()
    notes = models.TextField(blank=True,null=True)

    def __str__(self):
        return f"{self.exercise_name} {self.sets} {self.reps} {self.notes}"
