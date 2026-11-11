from django.contrib import admin
from .models import Member,WorkoutLog


admin.site.register(WorkoutLog)
admin.site.register(Member)
# new_member = Member(first_name='John',last_name='Doe',email='jhon@mail.com')
# new_member.save()
# all_members = Member.objects.all()
