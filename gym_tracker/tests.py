from django.test import TestCase
from django.urls import reverse
from .models import Member, WorkoutLog


class GymFlowTests(TestCase):
    def test_member_create_and_delete(self):
        response = self.client.post(reverse('member_add'), {
            'first_name': 'Dana', 'last_name': 'Levi', 'email': 'dana@example.com'
        })
        self.assertRedirects(response, reverse('member_list'))
        member = Member.objects.get(email='dana@example.com')
        self.assertContains(self.client.get(reverse('member_list')), 'dana@example.com')
        self.assertEqual(self.client.get(reverse('member_delete', args=[member.pk])).status_code, 405)
        self.client.post(reverse('member_delete', args=[member.pk]))
        self.assertFalse(Member.objects.filter(pk=member.pk).exists())

    def test_workout_create_and_delete(self):
        member = Member.objects.create(first_name='Dana', last_name='Levi', email='dana@example.com')
        response = self.client.post(reverse('workout_add'), {
            'member': member.pk, 'exercise_name': 'Squat', 'sets': 3, 'reps': 12, 'notes': 'ok'
        })
        self.assertRedirects(response, reverse('workout_list'))
        workout = WorkoutLog.objects.get(exercise_name='Squat')
        self.assertContains(self.client.get(reverse('workout_list')), 'Squat')
        self.client.post(reverse('workout_delete', args=[workout.pk]))
        self.assertFalse(WorkoutLog.objects.filter(pk=workout.pk).exists())

    def test_invalid_workout(self):
        member = Member.objects.create(first_name='Dana', last_name='Levi', email='dana@example.com')
        response = self.client.post(reverse('workout_add'), {
            'member': member.pk, 'exercise_name': 'Squat', 'sets': -1, 'reps': 0
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(WorkoutLog.objects.count(), 0)
