from django.urls import path
from . import views

urlpatterns = [
    path('', views.member_list, name='member_list'),
    path('members/add/', views.member_add, name='member_add'),
    path('members/<int:pk>/delete/', views.member_delete, name='member_delete'),
    path('workouts/', views.workout_list, name='workout_list'),
    path('workouts/add/', views.workout_add, name='workout_add'),
    path('workouts/<int:pk>/delete/', views.workout_delete, name='workout_delete'),
]
