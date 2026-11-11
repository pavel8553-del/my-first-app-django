from django import forms
from .models import Member, WorkoutLog


class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['first_name', 'last_name', 'email']
        labels = {'first_name': 'שם פרטי', 'last_name': 'שם משפחה', 'email': 'אימייל'}
        widgets = {'email': forms.EmailInput(attrs={'dir': 'ltr'})}


class WorkoutLogForm(forms.ModelForm):
    class Meta:
        model = WorkoutLog
        fields = ['member', 'exercise_name', 'sets', 'reps', 'notes']
        labels = {'member': 'מתאמן', 'exercise_name': 'תרגיל', 'sets': 'סטים',
                  'reps': 'חזרות', 'notes': 'הערות'}
        widgets = {'notes': forms.Textarea(attrs={'rows': 3}),
                   'sets': forms.NumberInput(attrs={'min': 1}),
                   'reps': forms.NumberInput(attrs={'min': 1})}

    def clean_sets(self):
        value = self.cleaned_data['sets']
        if value <= 0:
            raise forms.ValidationError('מספר הסטים חייב להיות חיובי')
        return value

    def clean_reps(self):
        value = self.cleaned_data['reps']
        if value <= 0:
            raise forms.ValidationError('מספר החזרות חייב להיות חיובי')
        return value
